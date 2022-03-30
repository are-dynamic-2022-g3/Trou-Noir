#Simulation constants
GRAVITY = 10
UPDATE_RATE = 1e-8
STARS_LIMITS = 50
SCREEN_WIDTH, SCREEN_HEIGHT = (1600,1000)


#Simulation parameters
number_of_stars = 45

size_min, size_max = 15, 95
size_to_blackhole = 75
size_to_whitedwarf = 5
lifespan_limit = 480 #ticks
lifespan_limit_RG = 240
lifespan_limit_RSG = 240
lifespan_limit_WD = 300 #ticks for white dwarf
vmin, vmax = 3, 6
blur_movement = True

#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

size_interpolation_speed = 5*1e6 
