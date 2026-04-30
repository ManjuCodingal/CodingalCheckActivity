# Space Invader with Music, Sounds, and Double Bullets

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
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Background Music
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)  # Loop forever

# Sound Effects
bullet_sound = pygame.mixer.Sound('laser.wav')
explosion_sound = pygame.mixer.Sound('bullet.wav')

# Create the screen
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

# Bullet
bulletImg = pygame.image.load('bullet.png')
bullets = []

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

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(
        (enemyX - bulletX) ** 2 +
        (enemyY - bulletY) ** 2
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

            if event.key == pygame.K_SPACE:
                # Play shooting sound
                bullet_sound.play()

                # Fire 2 bullets
                bullets.append([playerX + 5, playerY])
                bullets.append([playerX + 35, playerY])

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


        # Collision
        for bullet in bullets[:]:

            if isCollision(
                enemyX[i],
                enemyY[i],
                bullet[0],
                bullet[1]
            ):

                explosion_sound.play()

                bullets.remove(bullet)

                score_value += 1

                enemyX[i] = random.randint(
                    0,
                    SCREEN_WIDTH - 64
                )

                enemyY[i] = random.randint(
                    ENEMY_START_Y_MIN,
                    ENEMY_START_Y_MAX
                )

        enemy(enemyX[i], enemyY[i], i)


    # Bullet Movement
    for bullet in bullets[:]:

        bullet[1] -= BULLET_SPEED_Y

        screen.blit(
            bulletImg,
            (bullet[0], bullet[1])
        )

        if bullet[1] <= 0:
            bullets.remove(bullet)


    # Draw Player
    player(playerX, playerY)

    # Show Score
    show_score(10, 10)

    pygame.display.update()