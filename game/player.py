# game/player.py
import pygame
from game.config import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_IMG, PLAYER_SPEED, PLAYER_HP, RED

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load(PLAYER_IMG)
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = PLAYER_SPEED
        self.hp = PLAYER_HP
        self.max_hp = PLAYER_HP

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def update(self, screen_width, screen_height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # Draw hearts for HP
        for i in range(self.hp // 10):
            pygame.draw.rect(screen, RED, (10 + i * 35, 10, 30, 30))
