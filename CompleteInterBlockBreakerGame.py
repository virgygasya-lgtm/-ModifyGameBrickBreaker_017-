from py_compile import main

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

    class Ball:

    def __init__(self, x, y, size, speed):
        self.posx = x
        self.posy = y
        self.size = size
        self.speed = speed

        self.color = INTER_BLUE
        self.xFac = random.choice([-1, 1])
        self.yFac = -1

    def display(self):
        outer = pygame.Rect(
            int(self.posx - self.size / 2 - 2),
            int(self.posy - self.size / 2 - 2),
            self.size + 4,
            self.size + 4
        )

        pygame.draw.rect(screen, WHITE, outer)

        ballRect = pygame.Rect(
            int(self.posx - self.size / 2),
            int(self.posy - self.size / 2),
            self.size,
            self.size
        )

        pygame.draw.rect(screen, self.color, ballRect)

        pygame.draw.rect(
            screen, GOLD,
            (int(self.posx - 2), int(self.posy - 2), 4, 4)
        )

    def update(self):
        self.posx += self.xFac * self.speed
        self.posy += self.yFac * self.speed

        if self.posx <= self.size / 2:
            self.posx = self.size / 2
            self.xFac *= -1

        elif self.posx >= WIDTH - self.size / 2:
            self.posx = WIDTH - self.size / 2
            self.xFac *= -1

        if self.posy <= self.size / 2:
            self.posy = self.size / 2
            self.yFac *= -1

        if self.posy >= HEIGHT:
            return True

        return False

    def hit(self):
        self.yFac *= -1

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT - 100

        self.xFac = random.choice([-1, 1])
        self.yFac = -1

        self.color = random.choice(BALL_COLORS)

    def getRect(self):
        return pygame.Rect(
            int(self.posx - self.size / 2),
            int(self.posy - self.size / 2),
            self.size,
            self.size
        )

    class Block:

    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.health = 100

    def display(self):
        if self.health > 0:
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, WHITE, self.rect, 2)

            inner = self.rect.inflate(-10, -8)

            if inner.width > 0 and inner.height > 0:
                pygame.draw.rect(screen, GOLD, inner, 1)

    def hit(self):
        self.health -= 100

    def getRect(self):
        return self.rect


def collisionChecker(rect1, rect2):
    return rect1.colliderect(rect2)


def populateBlocks():
    blocks = []

    blockWidth = 40
    blockHeight = 20

    for x in range(0, WIDTH - blockWidth + 1, 60):
        for y in range(45, HEIGHT // 2, 35):
            color = random.choice(BLOCK_COLORS)

            blocks.append(
                Block(x, y, blockWidth, blockHeight, color)
            )

    return blocks 

    hitSound = None
breakSound = None

try:
    if pygame.mixer.get_init():
        if os.path.exists("hit.wav"):
            hitSound = pygame.mixer.Sound("hit.wav")

        if os.path.exists("break.wav"):
            breakSound = pygame.mixer.Sound("break.wav")
except pygame.error:
    pass


def playHitSound():
    if hitSound:
        hitSound.play()


def playBreakSound():
    if breakSound:
        breakSound.play()

        def main():
    running = True

    lives = 5
    score = 0

    striker = Striker(
        WIDTH // 2 - 50,
        HEIGHT - 50,
        100,
        20,
        10
    )

    ball = Ball(
        WIDTH // 2,
        HEIGHT - 100,
        16,
        5
    )

    blocks = populateBlocks()
    strikerDirection = 0

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    strikerDirection = -1
                elif event.key == pygame.K_RIGHT:
                    strikerDirection = 1

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    strikerDirection = 0

        # Score and lives
        scoreText = font.render(
            "SCORE: " + str(score), True, WHITE
        )

        livesText = font.render(
            "LIVES: " + str(lives), True, GOLD
        )

        title = font.render(
            "INTER MILAN EDITION", True, INTER_BLUE
        )

        screen.blit(scoreText, (15, 10))
        screen.blit(livesText, (180, 10))
        screen.blit(title, (380, 10))

        if not blocks:
            blocks = populateBlocks()

        # Magnet collision
        if collisionChecker(striker.getRect(), ball.getRect()):
            if ball.yFac > 0:
                ball.posy = striker.posy - ball.size / 2
                ball.hit()
                playHitSound()

                center = striker.posx + striker.width / 2

                if ball.posx < center:
                    ball.xFac = -1
                else:
                    ball.xFac = 1

        # Block collision
        for block in blocks[:]:
            if collisionChecker(block.getRect(), ball.getRect()):
                ball.hit()
                playHitSound()
                block.hit()

                if block.health <= 0:
                    blocks.remove(block)
                    score += 10
                    playBreakSound()

                break

        # Update game objects
        striker.update(strikerDirection)

        if ball.update():
            lives -= 1
            ball.reset()

        # Display blocks
        for block in blocks:
            block.display()

        striker.display()
        ball.display()

        if lives <= 0:
            screen.fill(BLACK)

            gameOverText = bigFont.render(
                "GAME OVER", True, RED
            )

            screen.blit(
                gameOverText,
                gameOverText.get_rect(
                    center=(WIDTH // 2, HEIGHT // 2)
                )
            )

            pygame.display.update()
            pygame.time.delay(2000)

            running = False

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()

    