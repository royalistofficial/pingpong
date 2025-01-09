import pygame
from game.ball import Ball
from game.paddle import Paddle
from config.config import BALL_D_SPEED, WIDTH, HEIGHT, BALL_SIZE


class CollisionHandler:
    def __init__(self, ball: Ball, paddle1: Paddle, paddle2: Paddle) -> None:
        self.ball = ball
        self.paddle1 = paddle1
        self.paddle2 = paddle2

    def checke_collisions(self) -> None:
        self._check_ball_paddle_collisions()
        self._check_ball_wall_collisions()
        self._check_ball_void_collisions()

    def _check_ball_paddle_collisions(self) -> None:
        def is_colliding_with_paddle(ball, paddle):
            return paddle.rect.top <= ball.rect.centery + \
                BALL_SIZE and ball.rect.centery - BALL_SIZE <= paddle.rect.bottom

        if (self.ball.rect.left <= self.paddle1.rect.right and
                is_colliding_with_paddle(self.ball, self.paddle1)):
            self.ball.speed_x = -self.ball.speed_x
            self.ball.speed_y -= (self.paddle1.rect.centery -
                                  self.ball.rect.centery) / 25
            self.ball.max_speed += BALL_D_SPEED
            self.ball.reset_speed()

        elif (self.ball.rect.right >= self.paddle2.rect.left and
                is_colliding_with_paddle(self.ball, self.paddle2)):
            self.ball.speed_x = -self.ball.speed_x
            self.ball.speed_y -= (self.paddle2.rect.centery -
                                  self.ball.rect.centery) / 25
            self.ball.max_speed += BALL_D_SPEED
            self.ball.reset_speed()

    def _check_ball_wall_collisions(self) -> None:
        if self.ball.rect.top <= 0 or self.ball.rect.bottom >= HEIGHT:
            self.ball.speed_y = -self.ball.speed_y

    def _check_ball_void_collisions(self) -> None:
        if self.ball.rect.left < 0:
            self.paddle2.score += 1
            self.ball.reset(False)
        elif self.ball.rect.right > WIDTH:
            self.paddle1.score += 1
            self.ball.reset(True)
