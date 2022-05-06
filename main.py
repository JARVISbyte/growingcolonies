# a main app file
import math
import numpy as np 
from api import Vector, distance
from theory import Colony, Map
from constants import *

""" 
    while True -> colonies.collide? colonies.update colonies.grow map.add.colony
"""

map = Map(AREA)
colony1 = Colony(Vector(-500, 100))
colony2 = Colony(Vector(100, 250))
colony3 = Colony(Vector(500, 500))

map.instances.extend((colony1, colony2, colony3))
# main loop 

for iteration in range(TIME_LIMIT*QUALITY):
    time = iteration/QUALITY
    # checking distances and future collides
    for colony_index, colony in enumerate(map.instances):
        colony.distances = np.full(len(map.instances), 0, dtype=np.float64)
        for next_colony_index in range(len(map.instances)): # range(a, b) = [a, b)
            #print(f"{colony_index} to {next_colony_index} :", distance(colony.pos, map.instances[next_colony_index].pos))
            if not colony_index == next_colony_index:
                next_colony = map.instances[next_colony_index]
                _distance = distance(colony.pos, next_colony.pos) - colony.radius - next_colony.radius
                colony.distances[next_colony_index] = _distance
                collide_time = _distance/(2*GROW_SPEED)
                # print(f'{colony_index} with {next_colony_index} : {collide_time}s')
                if collide_time <= DT:
                    colony.is_active = False
                    next_colony.is_active = False
        if colony.is_active:
            colony.radius += GROW_SPEED*DT
    
#print('\n'.join([f"{colony_index}: R: {colony.radius}mm ACTIVE: {colony.is_active}" for colony_index, colony in enumerate(map.instances)]))
#print('\n'.join([str(colony.distances) for colony in map.instances]))