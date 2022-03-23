from pygame import *
from typing import Tuple

def blur_screen(screen:Surface, alpha:int = 127, color:Tuple[int, int, int] = (0, 0, 0)) -> None:
    fadein = Surface((screen.get_width(), screen.get_height()))
    fadein = fadein.convert()
    fadein.fill(color)
    fadein.set_alpha(alpha)
    screen.blit(fadein, (0, 0))