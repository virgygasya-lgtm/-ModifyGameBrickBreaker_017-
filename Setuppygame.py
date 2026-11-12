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