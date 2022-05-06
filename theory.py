# a theory containing file
from api import *

class Colony:
    def __init__(self, position: Vector, radius: float = 1):
        self.radius = radius
        self.pos = position
        self.is_active = True
        self.distances = []
    
    @classmethod
    def collide(first, second) -> bool:
        return distance(first.pos, second.pos) <= first.radius + second.radius

class Map:
    def __init__(self, size):
        self.size = size
        self.instances = []
    #def spawn(self):
    #    self.instanses.append(Colony(Vector))