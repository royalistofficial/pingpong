import pygame
import sys
from game.game import Game, TwoPlayerGame, EasyOnePlayerGame, MediumOnePlayerGame, HardOnePlayerGame
from config.config import WIDTH, HEIGHT


class Menu:
    def __init__(
        self, font_size=74, font_color=(
            255, 255, 255), highlight_color=(
            255, 0, 0)):
        self.font = pygame.font.Font(None, font_size)
        self.main_menu_options = ["Начать игру", "Выход"]
        self.difficulty_menu_options = [
            "Легкий",
            "Средний",
            "Сложный",
            "Многопользовательская игра",
            "Назад"]
        self.selected_option = 0
        self.current_menu = "main"
        self.font_color = font_color
        self.highlight_color = highlight_color

        self.menu_actions = {
            "main": {
                0: self.start_game,
                1: self.exit_game
            },
            "difficulty": {
                0: lambda: EasyOnePlayerGame(),
                1: lambda: MediumOnePlayerGame(),
                2: lambda: HardOnePlayerGame(),
                3: lambda: TwoPlayerGame(),
                4: self.back_to_main
            }
        }

    def draw(self, window):
        window.fill((0, 0, 0))

        for y in range(HEIGHT):
            color = (0, 0 + int(255 * (y / HEIGHT)), 0)
            pygame.draw.line(window, color, (0, y), (WIDTH, y))

        options = self.get_current_options()

        for index, option in enumerate(options):
            color = self.highlight_color if index == self.selected_option else self.font_color
            text = self.font.render(option, True, color)
            window.blit( text,
                (WIDTH // 2 - text.get_width() // 2,
                 10 + index * 100))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (
                    self.selected_option - 1) % len(self.get_current_options())
            elif event.key == pygame.K_DOWN:
                self.selected_option = (
                    self.selected_option + 1) % len(self.get_current_options())
            elif event.key == pygame.K_RETURN:
                return self.select_option()

        return None

    def get_current_options(self):
        if self.current_menu == "main":
            return self.main_menu_options
        elif self.current_menu == "difficulty":
            return self.difficulty_menu_options


    def select_option(self):
        action = self.menu_actions[self.current_menu].get(self.selected_option)
        if action:
            return action()
        return None

    def start_game(self):
        self.current_menu = "difficulty"
        self.selected_option = 0
        return None

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def back_to_main(self):
        self.current_menu = "main"
        self.selected_option = 0
        return None
