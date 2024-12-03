import pygame
import sys
from config import WIDTH, HEIGHT
from game import Game


def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Пинг-понг")

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game = Game()

        game.handle_input()
        game.update()
        game.draw(window)

        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    main()
