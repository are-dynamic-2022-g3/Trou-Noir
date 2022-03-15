from mmap import ACCESS_DEFAULT
from pygame import *
import pygame.math

class Body():
    def __init__(self, pos = Vector2(0, 0), vel = Vector2(0, 0), acc = Vector2(0, 0), mass:float = 1, size:int = 1, color = (255, 255, 255)) -> None:
        self.position = pos
        self.velocity = vel
        self.acceleration = acc
        self.mass = mass
        self.size = size
        self.surface: Surface 
        self.color = color

    def update(self, delta:float) -> None:
        self.velocity.x += self.acceleration.x * delta
        self.velocity.y += self.acceleration.y * delta
        
        self.position.x += self.velocity.x * delta
        self.position.y += self.velocity.y * delta

    def get_image():
        pass