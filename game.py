import pygame
from paddle import Paddle
from ball import Ball
from config import WIDTH, HEIGHT, WHITE, BLACK, PADDLE_HEIGHT, PADDLE_WIDTH
from collision_handler import CollisionHandler


class Game:
    def __init__(self) -> None:
        self.paddle1 = Paddle(0, (HEIGHT - PADDLE_HEIGHT) // 2)
        self.paddle2 = Paddle(
            WIDTH - PADDLE_WIDTH,
            (HEIGHT - PADDLE_HEIGHT) // 2)
        self.ball = Ball()
        self.paused = False
        self.pause_key_pressed = False
        self.font = pygame.font.Font(None, 36)
        self.collision_handler = CollisionHandler(
            self.ball, self.paddle1, self.paddle2)

    def handle_input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p] and not self.pause_key_pressed:
            self.paused = not self.paused
            self.pause_key_pressed = True
        elif not keys[pygame.K_p]:
            self.pause_key_pressed = False

        if not self.paused:
            self.paddle1.move(pygame.K_w, pygame.K_s)
            self.paddle2.move(pygame.K_UP, pygame.K_DOWN)

    def update(self) -> None:
        if not self.paused:
            self.collision_handler.checke_collisions()
            self.ball.move()

    def draw(self, window: pygame.Surface) -> None:
        window.fill(BLACK)
        pygame.draw.rect(window, WHITE, self.paddle1.rect)
        pygame.draw.rect(window, WHITE, self.paddle2.rect)
        pygame.draw.ellipse(window, WHITE, self.ball.rect)

        score_text = self.font.render(
            f"{self.paddle1.score} - {self.paddle2.score}", True, WHITE)
        window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

        if self.paused:
            pause_text = self.font.render("PAUSED", True, WHITE)
            window.blit(
                pause_text,
                (WIDTH //
                 2 -
                 pause_text.get_width() //
                 2,
                 HEIGHT //
                 2 -
                 pause_text.get_height() //
                 2))

        pygame.display.flip()
