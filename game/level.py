# game/level.py
import pygame
from game.config import WHITE
from game.question_trigger import QuestionTrigger
from game.questions import get_random_question

class Level:
    def __init__(self, player):
        self.player = player
        self.obstacles = []
        self.question_triggers = []
        self.font = pygame.font.Font(None, 36)

    def add_obstacle(self, x, y, width, height, color):
        obstacle = pygame.Rect(x, y, width, height)
        self.obstacles.append((obstacle, color))
        
    def add_question_trigger(self, x, y, width, height, question):
        trigger = QuestionTrigger(x, y, width, height, question)
        self.question_triggers.append(trigger)

    def check_collisions(self):
        for obstacle, color in self.obstacles:
            if self.player.rect.colliderect(obstacle):
                # For simplicity, we just stop the player
                if self.player.rect.x < obstacle.x:
                    self.player.rect.right = obstacle.left
                if self.player.rect.x > obstacle.x:
                    self.player.rect.left = obstacle.right
                if self.player.rect.y < obstacle.y:
                    self.player.rect.bottom = obstacle.top
                if self.player.rect.y > obstacle.y:
                    self.player.rect.top = obstacle.bottom


    def draw(self, screen):
        for obstacle, color in self.obstacles:
            pygame.draw.rect(screen, color, obstacle)
        for trigger in self.question_triggers:
            trigger.draw(screen)

def create_level1(player):
    level = Level(player)
    level.add_obstacle(300, 400, 200, 50, WHITE)
    level.add_obstacle(500, 200, 50, 200, WHITE)
    level.add_question_trigger(600, 500, 50, 50, get_random_question())
    return level
