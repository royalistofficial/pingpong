import pygame
import sys
from config import WIDTH, HEIGHT
from game import Game
from menu import Menu

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Пинг-понг")

    game = Game()
    menu = Menu()
    in_menu = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if in_menu:
                action = menu.handle_input(event)
                if action == "start":
                    in_menu = False
            else:
                action = game.handle_input()
                if action == "menu":
                    in_menu = True

        if not in_menu:
            game.update()
            game.draw(window)
        else:
            menu.draw(window)

        pygame.time.Clock().tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main()
