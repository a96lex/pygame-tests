import pygame, sys
from engine.game import Game

Game.show_colors = True

while True:
    Game.main_loop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
