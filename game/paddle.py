import pygame
from game.ball import Ball
from abc import ABC, abstractmethod
from config.config import PADDLE_WIDTH, PADDLE_HEIGHT, HEIGHT, WIDTH, PADDLE_SPEED


class Paddle(ABC):
    def __init__(self, x: int, y: int) -> None:
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self._score: int = 0

    @abstractmethod
    def move(self) -> None:
        pass

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int = 1) -> None:
        self._score += value


class PlayerPaddle(Paddle):
    def __init__(self, x: int, y: int, up_key: int, down_key: int) -> None:
        super().__init__(x, y)
        self.up_key = up_key
        self.down_key = down_key

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[self.up_key] and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        if keys[self.down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED


class EasyBotPaddle(Paddle):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def move(self, ball: Ball) -> None:
        _, ball_y, _, _ = ball.get_state()

        tolerance = 10

        if self.rect.centery < ball_y - tolerance and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED
        elif self.rect.centery > ball_y + tolerance and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED


class MediumBotPaddle(Paddle):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def move(self, ball: Ball) -> None:
        ball_x, ball_y, ball_velocity_x, ball_velocity_y = ball.get_state()

        tolerance = 10

        if ball_velocity_x > 0:
            time_to_reach = (self.rect.x - ball_x) / ball_velocity_x
            predicted_ball_y = ball_y + ball_velocity_y * time_to_reach

            if predicted_ball_y < 0:
                predicted_ball_y = -predicted_ball_y
            elif predicted_ball_y > HEIGHT:
                predicted_ball_y = 2 * HEIGHT - predicted_ball_y

            if self.rect.centery < predicted_ball_y - \
                    tolerance and self.rect.bottom < HEIGHT:
                self.rect.y += PADDLE_SPEED
            elif self.rect.centery > predicted_ball_y + tolerance and self.rect.top > 0:
                self.rect.y -= PADDLE_SPEED
        else:
            if self.rect.centery < ball_y - tolerance and self.rect.bottom < HEIGHT:
                self.rect.y += PADDLE_SPEED
            elif self.rect.centery > ball_y + tolerance and self.rect.top > 0:
                self.rect.y -= PADDLE_SPEED


class HardBotPaddle(Paddle):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def move(self, ball: Ball) -> None:
        ball_x, ball_y, ball_velocity_x, ball_velocity_y = ball.get_state()

        if ball_velocity_x > 0:
            time_to_reach = (self.rect.x - ball_x) / ball_velocity_x
        else:
            time_to_reach = (WIDTH + ball_x) / abs(ball_velocity_x)

        predicted_ball_y = ball_y + ball_velocity_y * time_to_reach

        if predicted_ball_y < 0:
            predicted_ball_y = -predicted_ball_y
        elif predicted_ball_y > HEIGHT:
            predicted_ball_y = 2 * HEIGHT - predicted_ball_y

        tolerance = 10

        if self.rect.centery < predicted_ball_y - \
                tolerance and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED
        elif self.rect.centery > predicted_ball_y + tolerance and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
