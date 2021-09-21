import pygame
from engine.background import BackgroundChannel
from engine.gameConfig import GameConfig


pygame.init()
pygame.display.set_caption("Animated background")

display_size = (256, 192)
full_screen_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
scaling_factor = min(tuple(a / b for a, b in zip(full_screen_size, display_size)))


class Game(object):
    win = pygame.display.set_mode(full_screen_size)
    show_colors: bool = True
    bg: tuple = tuple(
        [
            BackgroundChannel(
                value=GameConfig.values[i],
                amount=GameConfig.amounts[i],
                sign=GameConfig.signs[i],
                position=i,
            )
            for i in range(3)
        ]
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
