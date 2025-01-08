import pygame
import sys
from config import WIDTH, HEIGHT

class Menu:
    def __init__(self):
        self.font = pygame.font.Font(None, 74)
        self.options = ["Начать игру", "Выбор сложности", "Выход"]
        self.selected_option = 0

    def draw(self, window):
        window.fill((0, 0, 0))
        for index, option in enumerate(self.options):
            if index == self.selected_option:
                text = self.font.render(option, True, (255, 0, 0))
            else:
                text = self.font.render(option, True, (255, 255, 255))
            window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + index * 100))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected_option == 0:
                    return "start"
                elif self.selected_option == 1:
                    return "difficulty"
                elif self.selected_option == 2:
                    pygame.quit()
                    sys.exit()

        return "menu"

class DifficultyMenu:
    def __init__(self):
        self.font = pygame.font.Font(None, 74)
        self.options = ["Однопользовательская игра", "Многопользовательская игра", "Назад"]
        self.selected_option = 0

    def draw(self, window):
        window.fill((0, 0, 0))
        for index, option in enumerate(self.options):
            if index == self.selected_option:
                text = self.font.render(option, True, (255, 0, 0))
            else:
                text = self.font.render(option, True, (255, 255, 255))
            window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + index * 100))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected_option == 0:
                    return "one_player"
                elif self.selected_option == 1:
                    return "two_player"
                elif self.selected_option == 2:
                    return "menu"

        return "difficulty"