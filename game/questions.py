# game/questions.py
import pygame
import random
from game.config import WHITE

QUESTIONS_DATA = [
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the color of the sky?",
        "options": ["Green", "Blue", "Red", "Yellow"],
        "answer": "Blue"
    }
]

class Question:
    def __init__(self, data):
        self.question = data["question"]
        self.options = data["options"]
        self.answer = data["answer"]
        self.font = pygame.font.Font(None, 36)
        self.selected_option = None

    def draw(self, screen):
        # Draw the question
        question_text = self.font.render(self.question, True, WHITE)
        screen.blit(question_text, (50, 100))

        # Draw the options
        for i, option in enumerate(self.options):
            option_text = self.font.render(f"{i + 1}. {option}", True, WHITE)
            screen.blit(option_text, (50, 150 + i * 50))

    def check_answer(self, selected_option_index):
        self.selected_option = self.options[selected_option_index]
        return self.selected_option == self.answer

def get_random_question():
    question_data = random.choice(QUESTIONS_DATA)
    return Question(question_data)
