#Simulation constants
GRAVITY = 1000
UPDATE_RATE = 1e-8
ticks_per_seconds = 20

#Simulation parameters
number_of_stars = 200
size_min, size_max = 1, 10
vmin, vmax = 5, 20
blur_movement = True #Better performance

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
