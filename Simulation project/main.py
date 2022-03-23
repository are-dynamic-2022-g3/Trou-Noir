from multiprocessing import Event
from random import randint, random, randrange
import pygame
from pygame import gfxdraw
from typing import List

from vfx import *
from body import *

SCREEN_WIDTH, SCREEN_HEIGHT = (1600,1000)

def apply_edge(b:Body) -> None:
  if b.position.x - b.size > SCREEN_WIDTH:
    b.velocity.x *= -1
  elif b.position.x + b.size < 0:
      b.velocity.x *= -1

  if b.position.y - b.size > SCREEN_HEIGHT:
    b.velocity.y *= -1
  elif b.position.y + b.size < 0:
     b.velocity.y *= -1


def draw_body(screen:Surface, b:Body) -> None:
  apply_edge(b)
  gfxdraw.filled_circle(screen, int(b.position.x), int(b.position.y), int(b.size), b.color)

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
            color = new_color)
    bodies.append(b)



  while run:
    ticks %= 60
    ticks += 1
    

    clock.tick(60)

    cursors_body.position = Vector2(pygame.mouse.get_pos())

    #Handle events
    for event in pygame.event.get():
      #Quit
      if event.type == pygame.QUIT: 
        run = False

      #Holding right click
      if event.type == pygame.MOUSEBUTTONDOWN: 
        is_clicking = True
      if event.type == pygame.MOUSEBUTTONUP:
        is_clicking = False

    if blur_movement:
      blur_screen(window)
    else:
      window.fill((0, 0, 0))


    #Apply forces
    l = range() if len(bodies) > STARS_LIMITS else range(len(bodies))
    for i in l:
      print(f"{i} < {len(bodies)}")
      if i >= len(bodies):
        continue
      b = bodies[i]
      b.acceleration = Vector2(0, 0)
      other:Body

      if is_clicking:
            b.apply_force_toward(cursors_body)
      for other in bodies:
        if b != other and b.distance(other) < 500:

          

          b.apply_force_toward(other)

          #Fusion
          if b.distance(other) < (b.size + other.size)/30:
            if b.size < other.size:
              temp = b
              other = b
              b = temp
            b.position = (b.position + other.position)/2
            b.mass += other.mass
            b.size += other.size
            bodies.remove(other)
          

      
      
      
    for b in bodies:
      b.update(UPDATE_RATE)
      apply_edge(b)
      draw_body(window, b)

    if ticks%20 == 1:
      text = font.render(f'FPS : {int(clock.get_fps())}|N = {len(bodies)}', True, white, black)
    window.blit(text, textRect)
      
      
    pygame.display.flip()




    

if __name__ == '__main__':
  main()
