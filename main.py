import pygame
import sys
from config import WIDTH, HEIGHT
from game import TwoPlayerGame, EasyOnePlayerGame, MediumOnePlayerGame
from menu import Menu


def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Пинг-понг")

    menu = Menu()
    game = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            action = menu.handle_input(event)
            if action == "Easy":
                game = EasyOnePlayerGame()
                menu.current_menu = "game"
            elif action == "Medium":
                game = MediumOnePlayerGame()
                menu.current_menu = "game"
            elif action == "two_player":
                game = TwoPlayerGame()
                menu.current_menu = "game"

        if menu.current_menu == "main" or menu.current_menu == "difficulty":
            menu.draw(window)
        elif menu.current_menu == "game":
            if game:
                action = game.handle_input()
                if action == "menu":
                    menu.current_menu = "main"
                    menu.selected_option = 0
                game.update()
                game.draw(window)

        pygame.time.Clock().tick(60)
        pygame.display.flip()


if __name__ == "__main__":
    main()
