from random import randint, random, randrange
import pygame
import math
from typing import List

from body import *

SCREEN_WIDTH, SCREEN_HEIGHT = (1600,1000)

def apply_edge(b:Body):
  if b.position.x - b.size > SCREEN_WIDTH:
    b.velocity.x *= -1
  elif b.position.x + b.size < 0:
      b.velocity.x *= -1

  if b.position.y - b.size > SCREEN_HEIGHT:
    b.velocity.y *= -1
  elif b.position.y + b.size < 0:
     b.velocity.y *= -1



def main():
  #pygame initialisation
  pygame.init()
  window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  #Variables
  bodies:List[Body] = []
  run = True
  is_clicking = False
  cursors_body:Body = Body(mass = 1e8)

  number_of_stars = 100
  size_min, size_max = 2, 10
  vmin, vmax = 5, 20

  #Generate random stars with parameters below
  for _ in range(number_of_stars):
    size = randint(size_min, size_max)
    b = Body(pos = Vector2(randint(size, SCREEN_WIDTH - size), randint(size, SCREEN_HEIGHT - size)), \
      vel = Vector2(random() * vmax + vmin, random() * vmax + vmin), \
        mass=size*50000, \
          size = size)
    bodies.append(b)



  while run:
    clock.tick(60)

    cursors_body.position = Vector2(pygame.mouse.get_pos())

    #EVENT
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        is_clicking = True
      if event.type == pygame.MOUSEBUTTONUP:
        is_clicking = False

    

    window.fill((0, 0, 0))

    #Apply forces
    for b in bodies:
      b.acceleration = Vector2(0, 0)
      other:Body
      for other in bodies:
        if b != other:
          b.apply_force_toward(other)

          if b.distance(other) < (b.size + other.size)/30:
            b.position = (b.position + other.position)/2
            b.velocity = (b.velocity + other.velocity)/2
            b.mass += other.mass
            b.size += other.size
            bodies.remove(other)
          

      if is_clicking:
        b.apply_force_toward(cursors_body)

      apply_edge(b)

      
      b.update(.0000001)
      
    #draw all bodies
    for b in bodies:
      pygame.draw.circle(window, b.color, b.position, b.size, 2)

    pygame.display.flip()




    

if __name__ == '__main__':
  main()
