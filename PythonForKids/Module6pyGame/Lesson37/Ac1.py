# To run code::py -3.10 "C:\Users\vishn\Documents\CodingalCheckActivity\PythonForKids\Module6pyGame\Lesson37\Ac1.py"
import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370 # Center the player horizontally (800/2 - 64/2)
PLAYER_START_Y = 380 # Position the player near the bottom of the screen (500 - 64 - 50)
ENEMY_START_Y_MIN = 50 # Minimum Y position for enemies to start
ENEMY_START_Y_MAX = 150 # Maximum Y position for enemies to start
ENEMY_SPEED_X = 4 # Speed at which enemies move horizontally. 4 units per frame is a good starting point for a moderate difficulty level.
ENEMY_SPEED_Y = 40 # Speed at which enemies move vertically.
BULLET_SPEED_Y = 10 # Speed at which bullets move vertically.
COLLISION_DISTANCE = 27 # Distance within which a collision is detected.

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('background.png')

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png') # ufo means unidentified flying object. The ufo icon is a small image that represents the game in the taskbar and window title bar. It adds a fun and thematic touch to the game, making it more visually appealing and recognizable to players.
pygame.display.set_icon(icon) # Set the window icon to a UFO image

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0 # Variable to track horizontal movement of the player. It starts at 0, meaning the player is stationary. When the left or right arrow keys are pressed, this variable will be updated to -5 or 5 respectively, causing the player to move left or right on the screen.

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))  # 64 is the size of the enemy
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)) # Randomly position the enemy within the specified Y range
    enemyX_change.append(ENEMY_SPEED_X) # Set the horizontal speed of the enemy. This will cause the enemy to move horizontally across the screen. The speed is set to 4 units per frame, which provides a moderate level of difficulty for players. You can adjust this value to make the game easier or harder as needed.
    enemyY_change.append(ENEMY_SPEED_Y) # Set the vertical speed of the enemy. This value determines how much the enemy moves downwards each time it hits the edge of the screen. A value of 40 means that every time an enemy reaches the left or right edge of the screen, it will move down by 40 pixels, creating a sense of progression and increasing difficulty as the game goes on. You can adjust this value to make the game easier or harder as needed.

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0 # Initial horizontal position of the bullet. This will be set to the player's current X position when the bullet is fired.
bulletY = PLAYER_START_Y # Initial vertical position of the bullet. This is set to the player's Y position so that the bullet appears to be fired from the player's location on the screen.
bulletX_change = 0 # Variable to track horizontal movement of the bullet. Since the bullet moves straight up, this value remains 0.
bulletY_change = BULLET_SPEED_Y # Variable to track vertical movement of the bullet. This value determines how fast the bullet moves upwards on the screen. A value of 10 means that the bullet will move up by 10 pixels each frame, creating a fast-moving projectile for the player to shoot at enemies. You can adjust this value to make the bullet faster or slower as needed.
bullet_state = "ready" # Variable to track the state of the bullet. It can be "ready" or "fire". When the bullet is in the "ready" state, it means that it is not currently visible on the screen and can be fired by the player. When the bullet is in the "fire" state, it means that it has been fired and is currently moving upwards on the screen. This variable helps to manage the firing mechanism and ensure that only one bullet can be fired at a time.

# Score
score_value = 0 # Variable to keep track of the player's score. It starts at 0 and increases by 1 each time the player successfully hits an enemy with a bullet. This variable is used to display the current score on the screen and can be used to determine the player's performance in the game. You can also implement additional features, such as increasing the score multiplier for consecutive hits or adding bonus points for certain achievements, to make the scoring system more engaging and rewarding for players.
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10 # Initial horizontal position for displaying the score on the screen. This value determines where the score will be displayed along the X-axis. A value of 10 means that the score will be displayed 10 pixels from the left edge of the screen, providing a clear and easily visible location for players to keep track of their score during the game.
textY = 10 # Initial vertical position for displaying the score on the screen. This value determines where the score will be displayed along the Y-axis. A value of 10 means that the score will be displayed 10 pixels from the top edge of the screen, providing a clear and easily visible location for players to keep track of their score during the game. You can adjust this value to move the score display higher or lower on the screen as needed.

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64) # Font object for displaying the "Game Over" text. This font is larger than the one used for the score to make it more prominent and attention-grabbing when the game ends. The size of 64 means that the text will be displayed in a large, bold font, making it clear to players that the game has ended. You can adjust this value to make the "Game Over" text larger or smaller as needed.

def show_score(x, y):
    # Display the current score on the screen.
    score = font.render("Score : " + str(score_value), True, (255, 255, 255)) # Render the score text using the font object. The text is created by concatenating the string "Score : " with the current score value, which is converted to a string. The second argument, True, enables anti-aliasing for smoother text rendering, and the third argument specifies the color of the text in RGB format (255, 255, 255) which is white. This function will be called in the game loop to continuously update and display the player's score on the screen.
    screen.blit(score, (x, y))

def game_over_text():
    # Display the game over text
    over_text = over_font.render("GAME OVER", True, (255, 255, 255)) # Render the "Game Over" text using the font object. The second argument, True, enables anti-aliasing for smoother text rendering, and the third argument specifies the color of the text in RGB format (255, 255, 255) which is white. This function will be called when the game ends to display the "Game Over" message on the screen.
    screen.blit(over_text, (200, 250))

def player(x, y):
    # Draw the player on the screen
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    # Draw an enemy on the screen
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    # Fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire" # Set the bullet state to "fire" to indicate that the bullet is currently active and moving upwards on the screen. This allows the game to manage the bullet's movement and collision detection while it is in flight.
    screen.blit(bulletImg, (x + 16, y + 10)) # Draw the bullet on the screen at the specified position. The bullet is drawn slightly offset from the player's position (x + 16, y + 10) to make it appear as if it is being fired from the center of the player's image. This creates a more visually appealing shooting effect, as the bullet will seem to originate from the player's character rather than from an arbitrary point on the screen.

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2) # Calculate the distance between the enemy and the bullet using the Pythagorean theorem. This formula computes the straight-line distance between two points (enemyX, enemyY) and (bulletX, bulletY) in a 2D space. The distance is calculated by taking the square root of the sum of the squared differences in the X and Y coordinates. This distance will be used to determine if a collision has occurred between the enemy and the bullet.
    return distance < COLLISION_DISTANCE # Return True if the distance is less than the defined collision distance, indicating that a collision has occurred. This means that the bullet has hit the enemy, and the game can then proceed to update the score, reset the bullet, and reposition the enemy as needed. If the distance is greater than or equal to the collision distance, it returns False, indicating that no collision has occurred and the game can continue without any changes to the score or enemy positions.

#Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0)) # Draw the background image on the screen at the top-left corner (0, 0). This will serve as the backdrop for the game, providing a visually appealing environment for the player and enemies. The background image will be displayed behind all other game elements, such as the player, enemies, and bullets, creating an immersive gaming experience.

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN: # Check if a key is pressed down. This event is triggered when the player presses any key on the keyboard. The game will listen for specific keys (left arrow, right arrow, and spacebar) to control the player's movement and shooting actions.
          if event.key == pygame.K_LEFT:
              playerX_change = -5
          if event.key == pygame.K_RIGHT:
              playerX_change = 5
          if event.key == pygame.K_SPACE and bullet_state == "ready": # Check if the spacebar is pressed and the bullet is in the "ready" state. This condition ensures that the player can only fire a bullet when there isn't already an active bullet on the screen. If the spacebar is pressed and the bullet is ready, it allows the player to shoot a new bullet from their current position.
              bulletX = playerX # Set the bullet's horizontal position to the player's current X position. This ensures that the bullet will be fired from the player's location on the screen, creating a more realistic shooting experience. When the player presses the spacebar to fire a bullet, the bulletX variable is updated to match the player's X coordinate, allowing the bullet to appear as if it is being shot from the player's position.
              fire_bullet(bulletX, bulletY)
      if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]: # Check if the left or right arrow key is released. This event is triggered when the player releases either the left or right arrow key, indicating that they want to stop moving in that direction. When this event occurs, the player's horizontal movement will be stopped by setting playerX_change back to 0.
          playerX_change = 0 # Set the player's horizontal movement to 0 when the left or right arrow key is released. This will stop the player from moving in that direction, allowing for more precise control over the player's movement. When the player releases the left or right arrow key, the playerX_change variable is reset to 0, which means that the player will no longer move horizontally until another key press is detected.

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  # 64 is the size of the player. This line ensures that the player's X position stays within the bounds of the screen. The max function prevents the player from moving left beyond the left edge of the screen (0), while the min function prevents the player from moving right beyond the right edge of the screen (SCREEN_WIDTH - 64). This keeps the player visible and allows for smooth movement across the screen without going off-screen.

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition. This condition checks if any enemy has moved down past a certain point on the screen (Y position greater than 340). If this happens, it means that the enemies have reached the player's area, and the game is considered over. When this condition is met, all enemies are moved off-screen by setting their Y positions to 2000, and the "Game Over" text is displayed on the screen. This effectively ends the game and prevents any further interactions with the enemies.
            for j in range(num_of_enemies): # Move all enemies off-screen when the game is over. This loop iterates through all the enemies and sets their Y positions to 2000, which is far below the visible area of the screen. This ensures that all enemies are effectively removed from the game when the "Game Over" condition is met, preventing any further interactions or collisions with the player.
                enemyY[j] = 2000 # Move the enemy off-screen by setting its Y position to 2000. This is done to ensure that the enemy is no longer visible or interactable in the game after the "Game Over" condition is met. By moving the enemy far below the visible area of the screen, it effectively removes the enemy from the game, allowing the "Game Over" text to be displayed without any distractions from remaining enemies.
            game_over_text()
            break

        enemyX[i] += enemyX_change[i] # Update the enemy's horizontal position by adding the horizontal speed (enemyX_change[i]) to its current X position (enemyX[i]). This will cause the enemy to move horizontally across the screen. The direction of movement will depend on the value of enemyX_change[i], which can be positive (moving right) or negative (moving left). This line is responsible for creating the movement of the enemies in the game, making them dynamic targets for the player to shoot at.
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64: # Check if the enemy has reached the left or right edge of the screen. This condition checks if the enemy's X position is less than or equal to 0 (left edge) or greater than or equal to SCREEN_WIDTH - 64 (right edge). If either condition is true, it means that the enemy has reached the edge of the screen and needs to change direction. When this happens, the enemy's horizontal speed (enemyX_change[i]) is multiplied by -1 to reverse its direction, and the enemy's Y position is increased by enemyY_change[i] to move it downwards, creating a more challenging gameplay experience as the enemies get closer to the player over time.
            enemyX_change[i] *= -1 # Reverse the enemy's horizontal direction by multiplying its horizontal speed (enemyX_change[i]) by -1. This will cause the enemy to move in the opposite direction when it reaches the edge of the screen, creating a bouncing effect as it moves back and forth across the screen.
            enemyY[i] += enemyY_change[i] # Move the enemy downwards by adding the vertical speed (enemyY_change[i]) to its current Y position (enemyY[i]). This will cause the enemy to move down the screen each time it hits the edge, increasing the difficulty of the game as the enemies get closer to the player over time. The combination of horizontal movement and vertical descent creates a dynamic and engaging gameplay experience for players as they try to shoot down the enemies before they reach the player's area.

        # Collision Check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready" # Reset the bullet's position and state after a collision is detected. This allows the player to fire a new bullet after successfully hitting an enemy. The bulletY variable is reset to the player's starting Y position, and the bullet_state is set back to "ready", indicating that the bullet is no longer active and can be fired again when the player presses the spacebar.
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64) # Reset the enemy's horizontal position to a random value within the screen bounds. This allows the enemy to reappear at a new location after being hit by a bullet, providing continuous gameplay and giving the player new targets to shoot at. The random.randint function is used to generate a random integer between 0 and SCREEN_WIDTH - 64, ensuring that the enemy's X position stays within the visible area of the screen.
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX) # Reset the enemy's vertical position to a random value within the specified Y range. This allows the enemy to reappear at a new vertical position after being hit by a bullet, adding variety to the gameplay and making it more challenging for the player. The random.randint function is used to generate a random integer between ENEMY_START_Y_MIN and ENEMY_START_Y_MAX, ensuring that the enemy's Y position stays within the defined range for enemy placement on the screen.

        enemy(enemyX[i], enemyY[i], i) # Draw the enemy on the screen at its updated position. This function call takes the enemy's current X and Y positions, as well as its index (i) to determine which enemy image to use from the enemyImg list. The enemy will be drawn at its new location after moving and potentially changing direction, allowing the player to see the updated position of the enemy as it moves across the screen.

    # Bullet Movement
    if bulletY <= 0: # Check if the bullet has moved off the top of the screen. This condition checks if the bullet's Y position is less than or equal to 0, which means that the bullet has reached the top edge of the screen and is no longer visible. When this happens, the bullet's position and state are reset to allow the player to fire a new bullet. The bulletY variable is reset to the player's starting Y position, and the bullet_state is set back to "ready", indicating that the bullet is no longer active and can be fired again when the player presses the spacebar.
        bulletY = PLAYER_START_Y
        bullet_state = "ready" # Reset the bullet's position and state after it moves off the top of the screen. This allows the player to fire a new bullet after the previous one has gone out of bounds. The bulletY variable is reset to the player's starting Y position, and the bullet_state is set back to "ready", indicating that the bullet is no longer active and can be fired again when the player presses the spacebar.
    elif bullet_state == "fire": # Check if the bullet is currently in the "fire" state, meaning it is active and moving upwards on the screen. If the bullet is in this state, it will be drawn on the screen at its current position, and its Y position will be updated to move it upwards. This allows the bullet to travel from the player's position towards the enemies, creating a dynamic shooting mechanic for the game.
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY) # Draw the player on the screen at its current position. This function call takes the player's current X and Y positions to determine where to draw the player image on the screen. The player will be drawn at its updated location after moving based on user input, allowing the player to see their character as they navigate and shoot at enemies in the game.
    show_score(textX, textY)
    pygame.display.update()