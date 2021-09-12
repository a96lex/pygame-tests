import sys
import pygame
from engine.background import bg_channel


pygame.init()
pygame.display.set_caption("Animated background")

display_size = (256, 192)
full_screen_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
scaling_factor = min(tuple(a / b for a, b in zip(full_screen_size, display_size)))


class Game(object):
    win = pygame.display.set_mode(full_screen_size)
    show_colors: bool = True
    bg: tuple = (
        bg_channel(value=100, amount=1, sign=1, position=0),
        bg_channel(value=140, amount=2, sign=-1, position=1),
        bg_channel(value=200, amount=3, sign=1, position=2),
    )

    @classmethod
    def main_loop(cls):
        pygame.time.delay(40)

        cls.win.fill(tuple(c.value for c in cls.bg))

        for color in cls.bg:
            color.update()
            if cls.show_colors:
                color.draw(cls.win)

        pygame.display.update()
