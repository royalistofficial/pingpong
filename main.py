import pygame
import sys
from config import WIDTH, HEIGHT
from game import Game, TwoPlayerGame, OnePlayerGame
from menu import Menu, DifficultyMenu

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Пинг-понг")

    menu = Menu()
    difficulty_menu = DifficultyMenu()
    in_menu = True
    in_difficulty_menu = False
    game = TwoPlayerGame()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if in_menu:
                action = menu.handle_input(event)
                if action == "start":
                    in_menu = False
                elif action == "difficulty":
                    in_menu = False
                    in_difficulty_menu = True
            elif in_difficulty_menu:
                action = difficulty_menu.handle_input(event)
                if action == "one_player":
                    game = OnePlayerGame()
                    in_difficulty_menu = False
                elif action == "two_player":
                    game = TwoPlayerGame()
                    in_difficulty_menu = False
                elif action == "menu":
                    in_difficulty_menu = False
                    in_menu = True
        

        if in_menu:
            menu.draw(window)
        elif in_difficulty_menu:
            difficulty_menu.draw(window)
        else:
            action = game.handle_input()
            if action == "menu":
                in_menu = True
            game.update()
            game.draw(window)

        pygame.time.Clock().tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main()