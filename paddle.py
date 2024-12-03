import pygame
from config import PADDLE_WIDTH, PADDLE_HEIGHT, HEIGHT, PADDLE_SPEED


class Paddle:
    def __init__(self, x: int, y: int) -> None:
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.score: int = 0

    def move(self, up_key: int, down_key: int) -> None:
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED
