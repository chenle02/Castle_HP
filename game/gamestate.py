# game/gamestate.py
from enum import Enum

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3

class GameStateManager:
    def __init__(self, initial_state):
        self.state = initial_state

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state
