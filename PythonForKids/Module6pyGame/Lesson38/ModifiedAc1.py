# 🚀 1. Add Multiple Bullets (Instead of One)
# Press SPACE → 2 bullets come out together
# They travel side-by-side
# Both can hit enemies independently

# ==CHANGES==
# 🔧 1. Removed Single-Bullet System
# ❌ You deleted this:
# bulletX = 0
# bulletY = PLAYER_START_Y
# bulletX_change = 0
# bulletY_change = BULLET_SPEED_Y
# bullet_state = "ready"
# 👉 Reason: This system only supports one bullet at a time
# 🔧 2. Added Bullet List
# ✅ Added this:
# bullets = []
# 👉 Now the game can store multiple bullets at once

# 🔧 3. Changed Firing Logic
# ❌ Original:
# if event.key == pygame.K_SPACE and bullet_state == "ready":
#     bulletX = playerX
#     fire_bullet(bulletX, bulletY)
# ✅ New:
# if event.key == pygame.K_SPACE:
#     bullets.append([playerX + 5, playerY])    # left bullet, +5 to position it on the left side of the player
#     bullets.append([playerX + 35, playerY])   # right bullet, +35 to position it on the right side of the player
# 👉 Now:
# No restriction (bullet_state removed)
# Fires two bullets at once

# 🔧 4. Removed fire_bullet() Usage
# ❌ This function is no longer used:
# def fire_bullet(x, y):
#     global bullet_state
#     bullet_state = "fire"
#     screen.blit(bulletImg, (x + 16, y + 10))
# 👉 Because now bullets are drawn inside a loop

# 🔧 5. Replaced Bullet Movement
# ❌ Original:
# if bulletY <= 0:
#     bulletY = PLAYER_START_Y
#     bullet_state = "ready"
# elif bullet_state == "fire":
#     fire_bullet(bulletX, bulletY)
#     bulletY -= bulletY_change
# ✅ New:
# for bullet in bullets[:]:  # : in [] to safely remove bullets while iterating
#     bullet[1] -= BULLET_SPEED_Y
#     screen.blit(bulletImg, (bullet[0], bullet[1]))

#     if bullet[1] <= 0:
#         bullets.remove(bullet)

# 👉 Now each bullet:
# Moves independently
# Gets removed when off-screen
# 🔧 6. Updated Collision Logic
# ❌ Original:
# if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
# ✅ New:
# for bullet in bullets[:]:
#     if isCollision(enemyX[i], enemyY[i], bullet[0], bullet[1]):
#         bullets.remove(bullet)

# 👉 Now:
# Every bullet is checked
# Any bullet can hit an enemy


# py -3.10 "C:\Users\vishn\Documents\CodingalCheckActivity\PythonForKids\Module6pyGame\Lesson38\ModifiedAc1.py"
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

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('background.png')

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

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# 🔥 MULTIPLE BULLETS
bulletImg = pygame.image.load('bullet.png')
bullets = []   # list to store bullets

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            # 🚀 FIRE TWO BULLETS
            if event.key == pygame.K_SPACE:
                bullets.append([playerX + 5, playerY])    # left bullet
                bullets.append([playerX + 35, playerY])   # right bullet

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # 🔥 COLLISION WITH ALL BULLETS
        for bullet in bullets[:]:
            if isCollision(enemyX[i], enemyY[i], bullet[0], bullet[1]):
                bullets.remove(bullet)
                score_value += 1
                enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
                enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # 🔥 BULLET MOVEMENT
    for bullet in bullets[:]:
        bullet[1] -= BULLET_SPEED_Y
        screen.blit(bulletImg, (bullet[0], bullet[1]))

        if bullet[1] <= 0:
            bullets.remove(bullet)

    player(playerX, playerY)
    show_score(10, 10)
    pygame.display.update()