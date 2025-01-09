import pygame
import sys
from config import WIDTH, HEIGHT


class Menu:
    def __init__(self):
        self.font = pygame.font.Font(None, 74)
        self.main_menu_options = ["Начать игру", "Выход"]
        self.difficulty_menu_options = [
            "Легкий",
            "Средний",
            "Сложный",
            "Многопользовательская игра",
            "Назад"]
        self.selected_option = 0
        self.current_menu = "main"

    def draw(self, window):
        window.fill((0, 0, 0))
        if self.current_menu == "main":
            options = self.main_menu_options
        else:
            options = self.difficulty_menu_options

        for index, option in enumerate(options):
            if index == self.selected_option:
                text = self.font.render(option, True, (255, 0, 0))
            else:
                text = self.font.render(option, True, (255, 255, 255))

            window.blit(
                text,
                (WIDTH // 2 -
                 text.get_width() // 2,
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

        return "menu"

    def get_current_options(self):
        if self.current_menu == "main":
            return self.main_menu_options
        else:
            return self.difficulty_menu_options

    def select_option(self):
        if self.current_menu == "main":
            if self.selected_option == 0:
                self.current_menu = "difficulty"
                self.selected_option = 0
            elif self.selected_option == 1:
                pygame.quit()
                sys.exit()
        elif self.current_menu == "difficulty":
            if self.selected_option == 0:
                return "Easy"
            elif self.selected_option == 1:
                return "Medium"
            elif self.selected_option == 2:
                return "Medium"
            elif self.selected_option == 3:
                return "two_player"
            elif self.selected_option == 4:
                self.current_menu = "main"
                self.selected_option = 0

        return self.current_menu
