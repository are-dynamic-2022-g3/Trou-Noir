from random import *
from typing import Tuple
from pygame import *
from constants import *

class BodyType():
    STAR = 0
    BLACKHOLE = 1
    OTHER = 2    

class Body():
    def __init__(self, pos:Vector2 = Vector2(0, 0), vel:Vector2 = Vector2(0, 0), acc:Vector2 = Vector2(0, 0), mass:float = 1, size:int = 1, color = (255, 255, 255), type:int = BodyType.STAR) -> None:
        self.position:Vector2 = pos
        self.velocity:Vector2 = vel
        self.acceleration:Vector2 = acc
        self.mass = mass
        self.size = size
        self.gfx_size = 0
        self.color = color
        self.type:int = type
        self.lifespan:int = 0

    def update(self, delta:float) -> None:
        """Update the body velocity, gfx size, and position"""
        self.gfx_size += (- self.gfx_size + self.size) >> 2 # <=> divide by 4
        self.velocity.x += self.acceleration.x * delta
        self.velocity.y += self.acceleration.y * delta
        
        self.position.x += self.velocity.x * delta
        self.position.y += self.velocity.y * delta

        self.lifespan += 1
        if random() < (self.lifespan  - lifespan_limit)/100:
            self.evolve()
            
    def apply_force_toward(self, other:super) -> None:
        """Apply force toward another body"""
        vec:Vector2 = other.position - self.position
        force = GRAVITY * other.mass/ vec.length()**2
        self.acceleration.x += vec.x * force
        self.acceleration.y += vec.y * force

    def kill(self):
        self.size = 0

    def become_blachole(self):
        self.type = BodyType.BLACKHOLE
        
    def evolve(self):
        if self.size > size_to_blackhole:
            self.become_blachole()
        else:
            self.kill()

    def distance(self, other:super) -> float:
        return (other.position - self.position).length()
        
    def get_image():
        pass

