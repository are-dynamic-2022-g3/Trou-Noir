#Simulation constants
from typing import Tuple


GRAVITY = 10
UPDATE_RATE = 1e-8
STARS_LIMITS = 50
SCREEN_WIDTH, SCREEN_HEIGHT = (1600,1000) 


#Simulation parameters
number_of_stars = 6
spawn_rate = .009

size_min, size_max = 15, 95
vmin, vmax = 0, 0
blur_movement = True

size_proportion_bh = 5

size_to_blackhole = 89
size_to_whitedwarf = 5


lifespan_limits = [480, 180, 180, -1, 300]
#STAR // REDGIANT // REDSUPERGIANT // BLACKHOLE // WHITEDWARF



#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

size_interpolation_speed = 5*1e6 

ColorT = Tuple[int, int, int]
