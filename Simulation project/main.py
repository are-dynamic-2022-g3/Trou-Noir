import pygame
import math
from typing import List

from body import *

SCREEN_WIDTH, SCREEN_HEIGHT = (1600,1000)


def main():
  #pygame initialisation
  pygame.init()
  window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  #Variables
  bodies:List[Body] = []
  run = True

  first_body = Body(size=10, vel = (3, 3))
  bodies.append(first_body)


  while run:

    #EVENT
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          quit()

      window.fill((0, 0, 0))

      for b in bodies:
        b.update(clock.tick())

      for b in bodies:
        pygame.draw.circle(window, b.color, b.position, b.size, 2)

      pygame.display.flip()
      


    

if __name__ == '__main__':
  main()
