from pickletools import TAKEN_FROM_ARGUMENT1
from numba import jit, cuda
from random import randint, random
import pygame
from pygame import gfxdraw
from typing import List

from vfx import *
from body import *



def apply_edge(b:Body) -> None:
  """
  if b.position.x - b.size > SCREEN_WIDTH:
    b.position.x = SCREEN_WIDTH + b.size
    b.velocity.x *= -1
  elif b.position.x + b.size < 0:
    b.position.x = - b.size
    b.velocity.x *= -1

  if b.position.y - b.size > SCREEN_HEIGHT:
    b.position.y = SCREEN_HEIGHT + b.size
    b.velocity.y *= -1
  elif b.position.y + b.size < 0:
    b.position.y = - b.size
    b.velocity.y *= -1
  """
  if b.position.x - b.size > SCREEN_WIDTH:
    b.position.x = -b.size
  elif b.position.x + b.size < 0:
    b.position.x = SCREEN_WIDTH + b.size

  if b.position.y - b.size > SCREEN_HEIGHT:
    b.position.y = -b.size
  elif b.position.y + b.size < 0:
    b.position.y = SCREEN_HEIGHT + b.size





def main():
  #pygame initialisation
  pygame.init()
  window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  #Variables
  bodies:List[Body] = []
  run = True
  is_clicking = False
  cursors_body:Body = Body(mass = 1e15)
  ticks = 0

  font = pygame.font.Font('freesansbold.ttf', 16)
  
  text = font.render(f'FPS : N/A', True, green, blue)
  textRect = text.get_rect()
  textRect.center = (50, 20)

  

  #Generate random stars with parameters below
  for _ in range(number_of_stars):
    new_color = randint(127, 255), randint(127, 255), randint(127, 255)
    size = randint(size_min, size_max)
    b = Body(pos = Vector2(randint(size, SCREEN_WIDTH - size), randint(size, SCREEN_HEIGHT - size)), \
      vel = Vector2(random() * vmax + vmin, random() * vmax + vmin), \
        mass=size*5e12, \
          size = size, \
            color = new_color, \
              type = randint(BodyType.STAR, BodyType.BLACKHOLE + 1)) 
    bodies.append(b)



  while run:
    ticks %= 60
    ticks += 1
    
    clock.tick(60)

    cursors_body.position = Vector2(pygame.mouse.get_pos())

    #===================================================================
    #Handle events
    for event in pygame.event.get():
      #Quit
      if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE): 
        run = False

      #Holding right click
      if event.type == pygame.MOUSEBUTTONDOWN: 
        is_clicking = True
      if event.type == pygame.MOUSEBUTTONUP:
        is_clicking = False

    if blur_movement:
      fade_screen(window, color = "#1E000E")
    else:
      window.fill((0, 0, 0))

    #===================================================================
    #Apply forces
    parts = len(bodies) // STARS_LIMITS
    l = range(STARS_LIMITS * (ticks % parts),\
       min(len(bodies), STARS_LIMITS * (1 + (ticks % parts))))\
          if len(bodies) > STARS_LIMITS \
            else range(len(bodies))
    for i in l:
      if i >= len(bodies):
        continue
      b = bodies[i]
      b.acceleration = Vector2(0, 0)
      other:Body

      if is_clicking:
            b.apply_force_toward(cursors_body)
      for other in bodies:
        if b != other and b.distance(other) < (b.size + other.size) * 3:

          b.apply_force_toward(other)

          #Merge
          if b.distance(other) < (b.size + other.size)/15:
            bigger, smaller = b, other
            if b.size < other.size:
              smaller, bigger = b, other
            bigger.mass += smaller.mass//3
            bigger.size += smaller.size//3
            bodies.remove(smaller)

    #===================================================================
    #Simualate and draw bodies
    for b in bodies:
      b.update(UPDATE_RATE)
      if b.gfx_size <= 0:
        bodies.remove(b)
        continue
      apply_edge(b)
      draw_body(window, b)

    #===================================================================
    #Show fps 
    if ticks%20 == 1:
      text = font.render(f'FPS : {int(clock.get_fps())}|N = {len(bodies)}', True, white, black)
    window.blit(text, textRect)
      
      
    pygame.display.flip()




    

if __name__ == '__main__':
  main()
