import numpy as np
import os
import PIL
import shutil
import unittest
import typing
from collections import defaultdict
from typing import Dict, Any, Optional, Set, List, Tuple
from flatland.envs.observations import TreeObsForRailEnv,GlobalObsForRailEnv
from flatland.envs.predictions import ShortestPathPredictorForRailEnv
from flatland.core.grid.grid4_utils import get_new_position
from flatland.utils.rendertools import RenderTool, AgentRenderVariant
from flatland.envs.agent_utils import EnvAgent
from flatland.envs.step_utils.states import TrainState
from flatland.envs.rail_env import RailEnv, RailEnvActions


def possible_actions_sorted_by_distance(env: RailEnv, handle: int):
    agent = env.agents[handle]
    

    if agent.state == TrainState.READY_TO_DEPART:
        agent_virtual_position = agent.initial_position
    elif agent.state.is_on_map_state():
        agent_virtual_position = agent.position
    else:
        print("no action possible!")
        print("agent status: ", agent.state)
        # NEW: if agent is at target, DO_NOTHING, and distance is zero.
        # NEW: (needs to be tested...)
        return [(RailEnvActions.DO_NOTHING, 0)] * 2

    possible_transitions = env.rail.get_transitions(*agent_virtual_position, agent.direction)
    print(f"possible transitions: {possible_transitions}")
    distance_map = env.distance_map.get()[handle]
    possible_steps = []
    for movement in list(range(4)):
        if possible_transitions[movement]:
            if movement == agent.direction:
                action = RailEnvActions.MOVE_FORWARD
            elif movement == (agent.direction + 1) % 4:
                action = RailEnvActions.MOVE_RIGHT
            elif movement == (agent.direction - 1) % 4:
                action = RailEnvActions.MOVE_LEFT
            else:
                print(f"An error occured. movement is: {movement}, agent direction is: {agent.direction}")
                if movement == (agent.direction + 2) % 4 or (movement == agent.direction - 2) % 4:
                    print("it seems that we are turning by 180 degrees. Turning in a dead end?")

                action = RailEnvActions.MOVE_FORWARD             
               
            distance = distance_map[get_new_position(agent_virtual_position, movement) + (movement,)]
            possible_steps.append((action, distance))
    possible_steps = sorted(possible_steps, key=lambda step: step[1])


    # if there is only one path to target, this is both the shortest one and the second shortest path.
    if len(possible_steps) == 1:
        return possible_steps * 2
    else:
        return possible_steps


class RailEnvWrapper:
  def __init__(self, env:RailEnv):
    self.env = env

    assert self.env is not None
    assert self.env.rail is not None, "Reset original environment first!"
    assert self.env.agents is not None, "Reset original environment first!"
    assert len(self.env.agents) > 0, "Reset original environment first!"

  # @property
  # def number_of_agents(self):
  #   return self.env.number_of_agents
  
  # @property
  # def agents(self):
  #   return self.env.agents

  # @property
  # def _seed(self):
  #   return self.env._seed

  # @property
  # def obs_builder(self):
  #   return self.env.obs_builder

  def __getattr__(self, name):
    try:
      return super().__getattr__(self,name)
    except:
      """Expose any other attributes of the underlying environment."""
      return getattr(self.env, name)


  @property
  def rail(self):
    return self.env.rail
  
  @property
  def width(self):
    return self.env.width
  
  @property
  def height(self):
    return self.env.height

  @property
  def agent_positions(self):
    return self.env.agent_positions

  def get_num_agents(self):
    return self.env.get_num_agents()

  def get_agent_handles(self):
    return self.env.get_agent_handles()

  def step(self, action_dict: Dict[int, RailEnvActions]):
    return self.env.step(action_dict)

  def reset(self, **kwargs):
    obs, info = self.env.reset(**kwargs)
    return obs, info


class ShortestPathActionWrapper(RailEnvWrapper):

    def __init__(self, env:RailEnv):
        super().__init__(env)
        
    def step(self, action_dict: Dict[int, RailEnvActions]) -> Tuple[Dict, Dict, Dict, Dict]:

      # input: action dict with actions in [0, 1, 2].
      transformed_action_dict = {}
      for agent_id, action in action_dict.items():
          if action == 0:
              transformed_action_dict[agent_id] = action
          else:
              #assert action in [1, 2]
              #assert possible_actions_sorted_by_distance(self.env, agent_id) is not None
              #assert possible_actions_sorted_by_distance(self.env, agent_id)[action - 1] is not None
              transformed_action_dict[agent_id] = possible_actions_sorted_by_distance(self.env, agent_id)[action - 1][0]

      obs, rewards, dones, info = self.env.step(transformed_action_dict)
      return obs, rewards, dones, info



def find_all_cells_where_agent_can_choose(env: RailEnv):
    """
    input: a RailEnv (or something which behaves similarly, e.g. a wrapped RailEnv),
    WHICH HAS BEEN RESET ALREADY!
    (o.w., we call env.rail, which is None before reset(), and crash.)
    """
    switches = []
    switches_neighbors = []
    directions = list(range(4))
    for h in range(env.height):
        for w in range(env.width):

            pos = (h, w)

            is_switch = False
            # Check for switch: if there is more than one outgoing transition
            for orientation in directions:
                possible_transitions = env.rail.get_transitions(*pos, orientation)
                num_transitions = np.count_nonzero(possible_transitions)
                if num_transitions > 1:
                    switches.append(pos)
                    is_switch = True
                    break
            if is_switch:
                # Add all neighbouring rails, if pos is a switch
                for orientation in directions:
                    possible_transitions = env.rail.get_transitions(*pos, orientation)
                    for movement in directions:
                        if possible_transitions[movement]:
                            switches_neighbors.append(get_new_position(pos, movement))

    decision_cells = switches + switches_neighbors
    return tuple(map(set, (switches, switches_neighbors, decision_cells)))


class NoChoiceCellsSkipper:
    def __init__(self, env:RailEnv, accumulate_skipped_rewards: bool, discounting: float) -> None:
      self.env = env
      self.switches = None
      self.switches_neighbors = None
      self.decision_cells = None
      self.accumulate_skipped_rewards = accumulate_skipped_rewards
      self.discounting = discounting
      self.skipped_rewards = defaultdict(list)

      # env.reset() can change the rail grid layout, so the switches, etc. will change! --> need to do this in reset() as well.
      #self.switches, self.switches_neighbors, self.decision_cells = find_all_cells_where_agent_can_choose(self.env)

      # compute and initialize value for switches, switches_neighbors, and decision_cells.
      self.reset_cells()

    def on_decision_cell(self, agent: EnvAgent) -> bool:
        return agent.position is None or agent.position == agent.initial_position or agent.position in self.decision_cells

    def on_switch(self, agent: EnvAgent) -> bool:
        return agent.position in self.switches

    def next_to_switch(self, agent: EnvAgent) -> bool:
        return agent.position in self.switches_neighbors

    def no_choice_skip_step(self, action_dict: Dict[int, RailEnvActions]) -> Tuple[Dict, Dict, Dict, Dict]:
        o, r, d, i = {}, {}, {}, {}
      
        # NEED TO INITIALIZE i["..."]
        # as we will access i["..."][agent_id]
        i["action_required"] = dict()
        i["malfunction"] = dict()
        i["speed"] = dict()
        i["status"] = dict() # TODO: change to "state"

        while len(o) == 0:
            obs, reward, done, info = self.env.step(action_dict)

            for agent_id, agent_obs in obs.items():
                if done[agent_id] or self.on_decision_cell(self.env.agents[agent_id]):
                    
                    o[agent_id] = agent_obs
                    r[agent_id] = reward[agent_id]
                    d[agent_id] = done[agent_id]

            
                    i["action_required"][agent_id] = info["action_required"][agent_id] 
                    i["malfunction"][agent_id] = info["malfunction"][agent_id]
                    i["speed"][agent_id] = info["speed"][agent_id]
                    i["status"][agent_id] = info["status"][agent_id] # TODO: change to "state"
                                                                  
                    if self.accumulate_skipped_rewards:
                        discounted_skipped_reward = r[agent_id]
                        for skipped_reward in reversed(self.skipped_rewards[agent_id]):
                            discounted_skipped_reward = self.discounting * discounted_skipped_reward + skipped_reward
                        r[agent_id] = discounted_skipped_reward
                        self.skipped_rewards[agent_id] = []

                elif self.accumulate_skipped_rewards:
                    self.skipped_rewards[agent_id].append(reward[agent_id])
                # end of for-loop

            d['__all__'] = done['__all__']
            action_dict = {}
            # end of while-loop

        return o, r, d, i

    
    def reset_cells(self) -> None:
        self.switches, self.switches_neighbors, self.decision_cells = find_all_cells_where_agent_can_choose(self.env)


# IMPORTANT: rail env should be reset() / initialized before put into this one!
class SkipNoChoiceCellsWrapper(RailEnvWrapper):
  
    # env can be a real RailEnv, or anything that shares the same interface
    # e.g. obs, rewards, dones, info = env.step(action_dict) and obs, info = env.reset(), and so on.
    def __init__(self, env:RailEnv, accumulate_skipped_rewards: bool, discounting: float) -> None:
        super().__init__(env)
        # save these so they can be inspected easier.
        self.accumulate_skipped_rewards = accumulate_skipped_rewards
        self.discounting = discounting
        self.skipper = NoChoiceCellsSkipper(env=self.env, accumulate_skipped_rewards=self.accumulate_skipped_rewards, discounting=self.discounting)

        self.skipper.reset_cells()

        self.switches = self.skipper.switches
        self.switches_neighbors = self.skipper.switches_neighbors
        self.decision_cells = self.skipper.decision_cells
        self.skipped_rewards = self.skipper.skipped_rewards

  
    def step(self, action_dict: Dict[int, RailEnvActions]) -> Tuple[Dict, Dict, Dict, Dict]:
        obs, rewards, dones, info = self.skipper.no_choice_skip_step(action_dict=action_dict)
        return obs, rewards, dones, info
        

    
    # arguments from RailEnv.reset() are: self, regenerate_rail: bool = True, regenerate_schedule: bool = True, activate_agents: bool = False, random_seed: bool = None
    def reset(self, **kwargs) -> Tuple[Dict, Dict]:
        obs, info = self.env.reset(**kwargs)
        # resets decision cells, switches, etc. These can change with an env.reset(...)!
        # needs to be done after env.reset().
        self.skipper.reset_cells()
        return obs, info