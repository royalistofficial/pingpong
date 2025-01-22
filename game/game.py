import pygame
from game.paddle import PlayerPaddle, EasyBotPaddle, MediumBotPaddle, HardBotPaddle
from abc import ABC, abstractmethod
from game.ball import Ball
from config.config import WIDTH, HEIGHT, WHITE, BLACK, PADDLE_HEIGHT, PADDLE_WIDTH
from collision.collision_handler import CollisionHandler


class Game(ABC):
    def __init__(self) -> None:
        self.paddle1 = None
        self.paddle2 = None
        self.ball = None
        self.collision_handler = None
        self.paused = False
        self.exit = False
        self.pause_key_pressed = False
        self.font = pygame.font.Font(None, 36)

    @abstractmethod
    def handle_input(self) -> str:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p] and not self.pause_key_pressed:
            self.paused = not self.paused
            self.pause_key_pressed = True
        elif not keys[pygame.K_p]:
            self.pause_key_pressed = False

        if keys[pygame.K_ESCAPE]:
            self.exit = True

    def update(self) -> None:
        if not self.paused:
            self.collision_handler.checke_collisions()
            self.ball.move()

    def draw(self, window: pygame.Surface) -> None:
        window.fill(BLACK)
        for y in range(HEIGHT):
            color = (0, 0, 0 + int(255 * (y / HEIGHT)))
            pygame.draw.line(window, color, (0, y), (WIDTH, y))

        pygame.draw.rect(window, WHITE, self.paddle1.rect)
        if self.paddle2:
            pygame.draw.rect(window, WHITE, self.paddle2.rect)
        pygame.draw.ellipse(window, WHITE, self.ball.rect)

        score_text = self.font.render(
            f"{self.paddle1.score} - {self.paddle2.score}", True, WHITE)
        window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

        if self.paused:
            pause_text = self.font.render("PAUSED", True, WHITE)
            window.blit(
                pause_text,
                (WIDTH // 2 -
                 pause_text.get_width() // 2,
                 HEIGHT // 2 -
                 pause_text.get_height() // 2))

        pygame.display.flip()


class TwoPlayerGame(Game):
    def __init__(self) -> None:
        super().__init__()
        self.paddle1 = PlayerPaddle(
            0, (HEIGHT - PADDLE_HEIGHT) // 2, pygame.K_w, pygame.K_s)
        self.paddle2 = PlayerPaddle(
            WIDTH - PADDLE_WIDTH
            (HEIGHT - PADDLE_HEIGHT) // 2,
            pygame.K_UP,
            pygame.K_DOWN)
        self.ball = Ball()
        self.collision_handler = CollisionHandler(
            self.ball, self.paddle1, self.paddle2)

    def handle_input(self) -> str:
        super().handle_input()

        if self.exit:
            return "menu"

        if not self.paused:
            self.paddle1.move()
            self.paddle2.move()

        return "game"


class EasyOnePlayerGame(Game):
    def __init__(self) -> None:
        super().__init__()
        self.paddle1 = PlayerPaddle(
            0, (HEIGHT - PADDLE_HEIGHT) // 2, pygame.K_w, pygame.K_s)
        self.paddle2 = EasyBotPaddle(
            WIDTH - PADDLE_WIDTH,
            (HEIGHT - PADDLE_HEIGHT) // 2)
        self.ball = Ball()
        self.collision_handler = CollisionHandler(
            self.ball, self.paddle1, self.paddle2)

    def handle_input(self) -> str:
        super().handle_input()

        if self.exit:
            return "menu"

        if not self.paused:
            self.paddle1.move()
            self.paddle2.move(self.ball)

        return "game"


class MediumOnePlayerGame(Game):
    def __init__(self) -> None:
        super().__init__()
        self.paddle1 = PlayerPaddle(
            0, (HEIGHT - PADDLE_HEIGHT) // 2,
            pygame.K_w, pygame.K_s)
        self.paddle2 = MediumBotPaddle(
            WIDTH - PADDLE_WIDTH,
            (HEIGHT - PADDLE_HEIGHT) // 2)
        self.ball = Ball()
        self.collision_handler = CollisionHandler(
            self.ball, self.paddle1, self.paddle2)

    def handle_input(self) -> str:
        super().handle_input()

        if self.exit:
            return "menu"

        if not self.paused:
            self.paddle1.move()
            self.paddle2.move(self.ball)

        return "game"


class HardOnePlayerGame(Game):
    def __init__(self) -> None:
        super().__init__()
        self.paddle1 = PlayerPaddle(
            0, (HEIGHT - PADDLE_HEIGHT) // 2,
            pygame.K_w, pygame.K_s)
        self.paddle2 = HardBotPaddle(
            WIDTH - PADDLE_WIDTH,
            (HEIGHT - PADDLE_HEIGHT) // 2)
        self.ball = Ball()
        self.collision_handler = CollisionHandler(
            self.ball, self.paddle1, self.paddle2)

    def handle_input(self) -> str:
        super().handle_input()

        if self.exit:
            return "menu"

        if not self.paused:
            self.paddle1.move()
            self.paddle2.move(self.ball)

        return "game"
