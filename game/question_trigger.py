# game/question_trigger.py
import pygame
from game.config import WHITE

class QuestionTrigger:
    def __init__(self, x, y, width, height, question):
        self.rect = pygame.Rect(x, y, width, height)
        self.question = question
        self.color = WHITE
        self.triggered = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
