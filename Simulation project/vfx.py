from pygame import *
from pygame import gfxdraw
from typing import Tuple

from body import *
from constants import *

class Background(sprite.Sprite):
    def __init__(self, image_file, location):
        sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image:Surface = image.load(image_file)
        self.rect:Rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def fade_screen(screen:Surface, alpha:int = 127, color:Tuple[int, int, int] = (0, 0, 0), background:Background = None) -> None:
    """Fade screen toward color
    screen -- the screen to fade in
    alpha -- The value of the fade in proportion (between 0 and 255)
    color -- Targeted color (default: Black)
    """
    fadein = Surface((screen.get_width(), screen.get_height()))
    fadein = fadein.convert()
    if background == None:
        fadein.fill(color)
    else:
        fadein.blit(background.image, background.rect)
    fadein.set_alpha(alpha)
    screen.blit(fadein, (0, 0))

def draw_body(screen:Surface, b:Body) -> None:
    """Draw the Body b into the Suface screen"""
    if b.type == BodyType.BLACKHOLE:
        draw.circle(screen,  b.gfxcolor, (int(b.position.x), int(b.position.y)),int(b.gfx_size), 5)
    else:
        gfxdraw.filled_circle(screen, int(b.position.x), int(b.position.y), int(b.gfx_size), b.gfxcolor)




