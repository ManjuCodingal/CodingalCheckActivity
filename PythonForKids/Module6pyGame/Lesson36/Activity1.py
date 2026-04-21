# To run code::py -3.10 "C:\Users\vishn\Documents\CodingalCheckActivity\PythonForKids\module6pyGame\Lesson36\Activity1.py"
# This code creates a simple Pygame application where the player controls a black rectangle (sprite1) using the arrow keys. The objective is to collide with a red rectangle (sprite2) to win the game. The background image is loaded and displayed, and the game runs until the player either wins or closes the window.
import pygame # Importing the Pygame library to create the game window and handle graphics and events. Pygame is a popular library for making games in Python, providing functionality for rendering graphics, handling user input, and managing game loops. Can be used for designing video games, simulations, and interactive applications.
import random

# Constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5 # The speed at which the player's sprite moves when arrow keys are pressed. Adjusting this value will make the sprite move faster or slower across the screen. 5 means that the sprite will move 5 pixels in the direction of the arrow key pressed each time the game loop updates. Increasing this value will make the sprite move more quickly, while decreasing it will slow down the movement.
FONT_SIZE = 72 # The size of the font used to display the "You win!" message when the player collides with the red rectangle. Adjusting this value will change how large or small the text appears on the screen. A value of 72 means that the font will be quite large, making the win message prominent and easy to read. Decreasing this value will make the text smaller, while increasing it will make it even larger.

# Initialize Pygame
pygame.init()

# Load and transform the background image
background_image = pygame.transform.scale(pygame.image.load("example.jpg"),
                                          (SCREEN_WIDTH, SCREEN_HEIGHT)) # transform.scale() is used to resize the loaded image to fit the dimensions of the game window defined by SCREEN_WIDTH and SCREEN_HEIGHT. This ensures that the background image fills the entire game window without distortion, regardless of its original size. The image is loaded from a file named "example.jpg" and then scaled to match the screen dimensions, providing a visually appealing backdrop for the game.

# Load font once at the beginning
font = pygame.font.SysFont("Times New Roman", FONT_SIZE) # pygame.font.SysFont() is used to create a Font object that can be used to render text in the game. The first argument specifies the font family (in this case, "Times New Roman"), and the second argument specifies the size of the font (defined by FONT_SIZE). This allows you to easily render text, such as the "You win!" message, with a consistent style and size throughout the game. By loading the font once at the beginning, you can efficiently reuse it whenever you need to display text on the screen without having to reload it each time.


class Sprite(pygame.sprite.Sprite): # This class defines a custom sprite that inherits from pygame.sprite.Sprite. It represents a rectangular object in the game that can be moved around and can collide with other sprites. The __init__ method initializes the sprite's image and rectangle, while the move method updates the sprite's position based on user input while ensuring it stays within the screen boundaries.

    def __init__(self, color, height, width): # The __init__ method is the constructor for the Sprite class. It initializes the sprite's image and rectangle based on the provided color, height, and width parameters. The method creates a surface for the sprite, fills it with a background color (dodgerblue), and then draws a rectangle of the specified color on top of it. Finally, it retrieves the rectangle that defines the sprite's position and size, which will be used for movement and collision detection in the game.
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(
            pygame.Color('dodgerblue'))  # Fill the sprite's surface with a background color (dodgerblue) to ensure that any transparent areas of the sprite are visible against the game background. This is important for visual clarity, especially if the sprite has a non-rectangular shape or if you want to create a specific visual effect. By filling the surface with a color, you can make sure that the sprite stands out and is easily distinguishable from the background and other game elements.
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change): # The move method updates the sprite's position based on the x_change and y_change values, which represent the movement in the horizontal and vertical directions, respectively. The method ensures that the sprite stays within the boundaries of the screen by using the max and min functions to limit the new position. This prevents the sprite from moving off-screen, allowing for a better gaming experience. The new position is calculated by adding the changes to the current position and then clamping it within the screen dimensions.
        self.rect.x = max(
            min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0) # self.rect.x + x_change calculates the new horizontal position of the sprite by adding the x_change value to the current x-coordinate. The min function ensures that this new position does not exceed the right edge of the screen (SCREEN_WIDTH - self.rect.width), while the max function ensures that it does not go below 0 (the left edge of the screen). This way, the sprite remains within the horizontal boundaries of the game window.
        # 0 is the minimum value for the y-coordinate, ensuring the sprite does not move above the top edge of the screen. SCREEN_HEIGHT - self.rect.height is the maximum value for the y-coordinate, ensuring the sprite does not move below the bottom edge of the screen. By using max and min functions, we ensure that the sprite's vertical position stays within the defined boundaries of the game window.
        self.rect.y = max(
            min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)


# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group() # A sprite group is a collection of sprites that can be managed together. In this code, all_sprites is created as an instance of pygame.sprite.Group(), which allows us to easily add, remove, and draw multiple sprites on the screen. By using a sprite group, we can efficiently handle the rendering and updates of all the sprites in the game without having to manage each one individually. This simplifies the code and improves performance when dealing with multiple sprites.

# Create sprites
sprite1 = Sprite(pygame.Color('black'), 20, 30) # This line creates an instance of the Sprite class named sprite1. The sprite is initialized with a black color, a height of 20 pixels, and a width of 30 pixels. This sprite will represent the player's character in the game, which can be moved around using the arrow keys. The color, height, and width parameters define the appearance of the sprite on the screen.
sprite1.rect.x, sprite1.rect.y = random.randint( # This line sets the initial position of sprite1 on the screen. The x-coordinate is assigned a random integer value between 0 and the maximum allowed value (SCREEN_WIDTH - sprite1.rect.width) to ensure that the sprite does not start off-screen. Similarly, the y-coordinate is assigned a random integer value between 0 and (SCREEN_HEIGHT - sprite1.rect.height) to keep the sprite within the vertical boundaries of the screen. This random placement adds an element of unpredictability to the game, making it more engaging for the player.
    0, SCREEN_WIDTH - sprite1.rect.width), random.randint( # The random.randint() function is used to generate a random integer for the x-coordinate of sprite1. The range is defined from 0 to (SCREEN_WIDTH - sprite1.rect.width) to ensure that the entire sprite fits within the horizontal boundaries of the screen. This prevents the sprite from being partially or fully off-screen when the game starts, providing a better gaming experience.
        0, SCREEN_HEIGHT - sprite1.rect.height) # The random.randint() function is used to generate a random integer for the y-coordinate of sprite1. The range is defined from 0 to (SCREEN_HEIGHT - sprite1.rect.height) to ensure that the entire sprite fits within the vertical boundaries of the screen. This prevents the sprite from being partially or fully off-screen when the game starts, allowing for a more engaging and visually appealing gaming experience.
all_sprites.add(sprite1)
    
sprite2 = Sprite(pygame.Color('red'), 20, 30) # This line creates another instance of the Sprite class named sprite2. The sprite is initialized with a red color, a height of 20 pixels, and a width of 30 pixels. This sprite will serve as the target that the player needs to collide with in order to win the game. The color, height, and width parameters define the appearance of this sprite on the screen, making it visually distinct from sprite1.
sprite2.rect.x, sprite2.rect.y = random.randint(
    0, SCREEN_WIDTH - sprite2.rect.width), random.randint(
        0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

# Game loop control variables
running, won = True, False
clock = pygame.time.Clock()

# Main game loop
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                         and event.key == pygame.K_x): # This line checks for events in the Pygame event queue. If the event type is pygame.QUIT (which occurs when the user clicks the close button on the window) or if the event type is pygame.KEYDOWN and the key pressed is pygame.K_x (the 'x' key), then the condition evaluates to True. In either case, it sets running to False, which will exit the main game loop and close the game window. This allows the player to quit the game either by closing the window or by pressing the 'x' key on the keyboard.
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] -keys[pygame.K_LEFT]) * MOVEMENT_SPEED # This line calculates the horizontal movement (x_change) for sprite1 based on the current state of the arrow keys. It checks if the right arrow key (pygame.K_RIGHT) is pressed and subtracts the state of the left arrow key (pygame.K_LEFT). If the right arrow key is pressed, it contributes a value of 1, and if the left arrow key is pressed, it contributes a value of -1. The resulting value is then multiplied by MOVEMENT_SPEED to determine how much sprite1 should move horizontally in the current frame. This allows for smooth movement of sprite1 in response to user input.
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect): # This line checks for a collision between sprite1 and sprite2 using the colliderect() method. It compares the rectangles of both sprites to see if they overlap. If the rectangles collide, it means that sprite1 has successfully reached sprite2, which is the winning condition for the game. When this happens, sprite2 is removed from the all_sprites group, and the won variable is set to True, indicating that the player has won the game.
            all_sprites.remove(sprite2)
            won = True

    # Drawing
    screen.blit(background_image, (0, 0)) # This line draws the background image onto the screen at the coordinates (0, 0), which is the top-left corner of the game window. The blit() method is used to copy the background image onto the screen surface, effectively setting it as the backdrop for the game. This ensures that the background is displayed behind all other sprites and game elements, creating a visually appealing environment for the player.
    all_sprites.draw(screen)

    # Display win message
    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2,
                               (SCREEN_HEIGHT - win_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
