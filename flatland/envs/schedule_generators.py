import os
import json
import itertools
import warnings
from typing import Tuple, List, Callable, Mapping, Optional, Any
from flatland.envs.schedule_utils import Schedule

import numpy as np
from numpy.random.mtrand import RandomState

from flatland.envs.agent_utils import EnvAgent
from flatland.envs.distance_map import DistanceMap
from flatland.envs.rail_env_shortest_paths import get_shortest_paths


def schedule_generator(agents: List[EnvAgent], config_speeds: List[float],  distance_map: DistanceMap, 
                            agents_hints: dict, np_random: RandomState = None) -> Schedule:

    # max_episode_steps calculation
    if agents_hints:
        city_positions = agents_hints['city_positions']
        num_cities = len(city_positions)
    else:
        num_cities = 2

    timedelay_factor = 4
    alpha = 2
    max_episode_steps = int(timedelay_factor * alpha * \
        (distance_map.rail.width + distance_map.rail.height + (len(agents) / num_cities)))
    
    # Multipliers
    old_max_episode_steps_multiplier = 3.0
    new_max_episode_steps_multiplier = 1.5
    travel_buffer_multiplier = 1.3 # must be strictly lesser than new_max_episode_steps_multiplier
    end_buffer_multiplier = 0.05
    mean_shortest_path_multiplier = 0.2
    
    shortest_paths = get_shortest_paths(distance_map)
    shortest_paths_lengths = [len(v) for k,v in shortest_paths.items()]

    # Find mean_shortest_path_time
    agent_shortest_path_times = []
    for agent in agents:
        speed = agent.speed_data['speed']
        distance = shortest_paths_lengths[agent.handle]
        agent_shortest_path_times.append(int(np.ceil(distance / speed)))

    mean_shortest_path_time = np.mean(agent_shortest_path_times)

    # Deciding on a suitable max_episode_steps
    max_sp_len = max(shortest_paths_lengths) # longest path
    min_speed = min(config_speeds)           # slowest possible speed in config
    
    longest_sp_time = max_sp_len / min_speed
    max_episode_steps_new = int(np.ceil(longest_sp_time * new_max_episode_steps_multiplier))
    
    max_episode_steps_old = int(max_episode_steps * old_max_episode_steps_multiplier)

    max_episode_steps = min(max_episode_steps_new, max_episode_steps_old)
    
    end_buffer = int(max_episode_steps * end_buffer_multiplier)
    latest_arrival_max = max_episode_steps-end_buffer

    # Useless unless needed by returning
    earliest_departures = []
    latest_arrivals = []

    for agent in agents:
        agent_shortest_path_time = agent_shortest_path_times[agent.handle]
        agent_travel_time_max = int(np.ceil((agent_shortest_path_time * travel_buffer_multiplier) \
                                            + (mean_shortest_path_time * mean_shortest_path_multiplier)))
        
        departure_window_max = max(latest_arrival_max - agent_travel_time_max, 1)
        
        earliest_departure = np_random.randint(0, departure_window_max)
        latest_arrival = earliest_departure + agent_travel_time_max
        
        earliest_departures.append(earliest_departure)
        latest_arrivals.append(latest_arrival)

        agent.earliest_departure = earliest_departure
        agent.latest_arrival = latest_arrival

    return Schedule(earliest_departures=earliest_departures, latest_arrivals=latest_arrivals,
                    max_episode_steps=max_episode_steps)
