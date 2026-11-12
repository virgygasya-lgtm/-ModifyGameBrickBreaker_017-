import pygame
import random
import os

pygame.init()

try:
    pygame.mixer.init()
except pygame.error:
    pass

WIDTH, HEIGHT = 600, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("INTER MILAN - MAGNETIC BLOCK BREAKER")

clock = pygame.time.Clock()
FPS = 30

font = pygame.font.Font(None, 25)
bigFont = pygame.font.Font(None, 45)

BLACK = (5, 5, 15)
INTER_BLUE = (0, 80, 180)
DARK_BLUE = (0, 35, 90)
WHITE = (255, 255, 255)
GOLD = (220, 180, 70)
RED = (210, 30, 50)

BALL_COLORS = [
    INTER_BLUE,
    DARK_BLUE,
    BLACK,
    GOLD
]

BLOCK_COLORS = [
    INTER_BLUE,
    DARK_BLUE,
    GOLD
]

class Striker:

    def __init__(self, posx, posy, width, height, speed):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed

        self.rect = pygame.Rect(
            posx, posy, width, height
        )

    def display(self):
        pygame.draw.rect(screen, INTER_BLUE, self.rect)

        pygame.draw.rect(
            screen, RED,
            (self.posx, self.posy, 15, self.height)
        )

        pygame.draw.rect(
            screen, WHITE,
            (self.posx + self.width - 15,
             self.posy, 15, self.height)
        )

        text = pygame.font.Font(None, 17).render(
            "INTER MAGNET", True, WHITE
        )

        screen.blit(text, text.get_rect(center=self.rect.center))

    def update(self, direction):
        self.posx += self.speed * direction

        self.posx = max(
            0,
            min(WIDTH - self.width, self.posx)
        )

        self.rect.x = self.posx

    def getRect(self):
        return self.rect
    