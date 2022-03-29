from pygame import *
from pygame import gfxdraw
from typing import Tuple
from body import *
from constants import *

def fade_screen(screen:Surface, alpha:int = 127, color:Tuple[int, int, int] = (0, 0, 0)) -> None:
    """Fade screen toward color
    screen -- the screen to fade in
    alpha -- The value of the fade in proportion (between 0 and 255)
    color -- Targeted color (default: Black)
    """
    fadein = Surface((screen.get_width(), screen.get_height()))
    fadein = fadein.convert()
    fadein.fill(color)
    fadein.set_alpha(alpha)
    screen.blit(fadein, (0, 0))

def draw_body(screen:Surface, b:Body) -> None:
    """Draw the Body b into the Suface screen"""
    if b.type == BodyType.BLACKHOLE:
        gfxdraw.aacircle(screen, int(b.position.x), int(b.position.y), int(b.gfx_size), b.color)
    else:
        gfxdraw.filled_circle(screen, int(b.position.x), int(b.position.y), int(b.gfx_size), b.color)
