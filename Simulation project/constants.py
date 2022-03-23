#Simulation constants
GRAVITY = 10
UPDATE_RATE = 1e-8
STARS_LIMITS = 25


#Simulation parameters
number_of_stars = 100

size_min, size_max = 1, 10
vmin, vmax = 5, 20
blur_movement = True

#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

class BodyType:
    STAR = 0
    BLACKHOLE = 1
    OTHER = 2
