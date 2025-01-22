import pygame
import sys
from config.config import WIDTH, HEIGHT
from game.game import Game, TwoPlayerGame, EasyOnePlayerGame, MediumOnePlayerGame, HardOnePlayerGame
from menu.menu import Menu

def handle_events(menu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        action = menu.handle_input(event)
        if isinstance(action, Game): 
            menu.current_menu = "game"
            return action
    return None

def update_menu(menu, game, window):
    if menu.current_menu == "game" and game:
        action = game.handle_input()
        if action == "menu":
            menu.current_menu = "main"
            menu.selected_option = 0
        game.update()
        game.draw(window)
    else:
        menu.draw(window)

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Пинг-понг")

    menu = Menu()
    game = None

    while True:
        game = handle_events(menu) or game
        update_menu(menu, game, window)

        pygame.time.Clock().tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main()