import pygame
import random
from config import BALL_SIZE, BALL_SPEED, WIDTH, HEIGHT, PADDLE_WIDTH


class Ball:
    def __init__(self) -> None:
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.reset()

    def reset_speed(self) -> None:
        self.max_speed = min(self.max_speed, PADDLE_WIDTH)
        norm = (self.speed_x ** 2 + self.speed_y ** 2) ** 0.5
        self.speed_x = (self.speed_x / norm) * self.max_speed
        self.speed_y = (self.speed_y / norm) * self.max_speed

    def move(self) -> None:
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def reset(self, dir=True) -> None:
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        self.max_speed = BALL_SPEED
        self.speed_x = 1 if dir else -1
        self.speed_y = 0
        self.reset_speed()
