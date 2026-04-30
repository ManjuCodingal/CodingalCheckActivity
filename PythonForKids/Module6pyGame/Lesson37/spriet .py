# Space Invader — Score increases when Player collides with Enemy

import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
COLLISION_DISTANCE = 40   # slightly bigger for player collision

# Initialize Pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('background.png')

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render(
        "Score : " + str(score_value),
        True,
        (255, 255, 255)
    )
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render(
        "GAME OVER",
        True,
        (255, 255, 255)
    )
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def isCollision(x1, y1, x2, y2):
    distance = math.sqrt(
        (x1 - x2) ** 2 +
        (y1 - y2) ** 2
    )
    return distance < COLLISION_DISTANCE


# Game Loop
running = True

while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Key Press
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        # Key Release
        if event.type == pygame.KEYUP:

            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0


    # Player Movement
    playerX += playerX_change

    if playerX < 0:
        playerX = 0

    if playerX > SCREEN_WIDTH - 64:
        playerX = SCREEN_WIDTH - 64


    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 340:

            for j in range(num_of_enemies):
                enemyY[j] = 2000

            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = ENEMY_SPEED_X
            enemyY[i] += ENEMY_SPEED_Y

        elif enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] = -ENEMY_SPEED_X
            enemyY[i] += ENEMY_SPEED_Y


        # Player–Enemy Collision
        if isCollision(
            playerX,
            playerY,
            enemyX[i],
            enemyY[i]
        ):

            score_value += 1

            # Respawn enemy
            enemyX[i] = random.randint(
                0,
                SCREEN_WIDTH - 64
            )

            enemyY[i] = random.randint(
                ENEMY_START_Y_MIN,
                ENEMY_START_Y_MAX
            )

        enemy(enemyX[i], enemyY[i], i)


    # Draw Player
    player(playerX, playerY)

    # Show Score
    show_score(10, 10)

    pygame.display.update()