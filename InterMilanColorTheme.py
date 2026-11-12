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