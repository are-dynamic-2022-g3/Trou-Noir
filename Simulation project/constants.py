#Simulation constants
from typing import Tuple


GRAVITY = 1e5
UPDATE_RATE = 1e-10
STARS_LIMITS = 50
SCREEN_WIDTH, SCREEN_HEIGHT = (1600,1000) 
SIZE_TO_MASS_FACTOR = 5e12


#Simulation parameters
number_of_stars = 12
spawn_rate = .024

size_min, size_max = 12, 69 #Size with what the stars with spawn = randint(size_min, size_max)
vmin, vmax = 0, 0 #Range of the initial velocity
blur_movement = True #Visual effect
blur_intesity = 128
visibilty = False

size_proportion_bh = .2 #Blackhole seem smaller than they are

size_to_blackhole = 55
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
