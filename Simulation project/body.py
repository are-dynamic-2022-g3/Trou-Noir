from random import *
from pygame import *

from constants import *
from operation import *
from data import *

class BodyType():
    STAR = 0
    REDGIANT= 1 #va devenir white dwarf (plus petite)
    REDSUPERGIANT = 2 #va devenir trou noir (plus grande)
    BLACKHOLE = 3
    WHITEDWARF = 4

class Body():
    def __init__(self, pos:Vector2 = Vector2(0, 0), vel:Vector2 = Vector2(0, 0), acc:Vector2 = Vector2(0, 0), mass:float = 1, size:int = 1, color = (255, 255, 255), type:int = BodyType.STAR) -> None:
        self.position:Vector2 = pos
        self.velocity:Vector2 = vel
        self.acceleration:Vector2 = acc
        self.mass = mass
        self.size:int = size
        self.gfx_size:int = 0
        self.color = color
        self.gfx_color = white
        self.type:int = type
        self.lifespan:int = 0

    def update(self, delta:float) -> None:
        """Update the body velocity, gfx size, and position"""
        self.gfx_size += int(- self.gfx_size + self.size * (1 - int(self.type == BodyType.BLACKHOLE) * (1 - size_proportion_bh))) >> 2 # <=> divide by 4
        self.gfx_color = mean_color(self.gfx_color, self.color)


        self.velocity.x += self.acceleration.x * delta
        self.velocity.y += self.acceleration.y * delta
        
        self.position.x += self.velocity.x * delta
        self.position.y += self.velocity.y * delta

        if self.lifespan >= 0:
            self.lifespan += 1
        if random() < (self.lifespan  - lifespan_limits[self.type])/1000:
            self.evolve()

        if self.type == BodyType.BLACKHOLE:
            self.mass *= .9997

            self.size = self.mass // SIZE_TO_MASS_FACTOR
            
    def apply_force_toward(self, other:super) -> None:
        """Apply force toward another body"""
        vec:Vector2 = other.position - self.position
        force = GRAVITY * other.mass/ vec.length()**2
        self.acceleration.x += vec.x * force
        self.acceleration.y += vec.y * force

    def kill(self):
        self.size = 0
        if self.type == BodyType.BLACKHOLE:
            current_data[DataType.NumberOfBlackHole] -= 1
        else:
            current_data[DataType.NumberOfStars] -= 1

    def become_redgiant(self):
        self.type = BodyType.REDGIANT
        new_color_RG = randint(205, 255), randint(37, 49), randint(37, 47)
        self.color = new_color_RG
        self.lifespan = 0

    def become_red_super_giant(self):
        self.type = BodyType.REDSUPERGIANT
        new_color_RSG = randint(235, 255), randint(115, 140), 0
        self.color = new_color_RSG
        self.lifespan = 0

    def become_blachole(self):
        self.type = BodyType.BLACKHOLE
        new_color_BH = randint(102, 127), randint(18, 24), randint(16, 23) #black hole color = red
        self.color = new_color_BH 
        self.lifespan = -1
        current_data[DataType.NumberOfBlackHole] += 1
        current_data[DataType.NumberOfStars] -= 1
        
    def become_whitedwarf(self):
        self.type = BodyType.WHITEDWARF 
        new_color_WD = randint(200, 255), 255 , 255 #white dwarf color = white
        self.color = new_color_WD 
        self.size = size_to_whitedwarf
        self.mass /= 8
        self.lifespan = 0

    def evolve(self):
        if self.type == BodyType.REDSUPERGIANT:
            self.become_blachole()
        elif self.type == BodyType.REDGIANT:
            self.become_whitedwarf()
        elif self.type == BodyType.WHITEDWARF:
            self.kill()
        elif self.size > size_to_blackhole: 
            self.become_red_super_giant()
        else:
            self.become_redgiant()

    def distance(self, other:super) -> float:
        return (other.position - self.position).length()
        
    def get_image():
        pass

