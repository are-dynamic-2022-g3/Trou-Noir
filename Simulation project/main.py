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

  font = pygame.font.Font('freesansbold.ttf', 32)
  textRect = text.get_rect()
  textRect.center = (0, 0)

  

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
    clock.tick(144)

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
    for b in bodies:
      b.acceleration = Vector2(0, 0)
      other:Body
      for other in bodies:
        if b != other:
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
          

      if is_clicking:
        b.apply_force_toward(cursors_body)

      apply_edge(b)
      b.update(UPDATE_RATE)
      
    for b in bodies:
      draw_body(window, b)

    text = font.render(f'FPS : {clock.get_fps}', True, green, blue)
    window.blit(text, textRect)
      
      
    pygame.display.flip()




    

if __name__ == '__main__':
  main()
