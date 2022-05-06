# api file: useful classes and functions
from ctypes import Union

from math import sqrt


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
    def lenght(self) -> float:
        return sqrt(self.x**2 + self.y**2)

def distance(Va, Vb):
    return sqrt( (Va.x - Vb.x)**2 + (Va.y - Vb.y)**2 )

