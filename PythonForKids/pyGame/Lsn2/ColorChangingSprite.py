# To run code:: py -3.10 "C:\Users\vishn\Documents\CodingalCheckActivity\PythonForKids\pyGame\Lsn2\COlorChangingSprite.py"

# In game design, a sprite is a 2D image or animation used to represent characters, objects, or effects on the screen. Classic games (like old arcade games) used sprites for everything you see moving.
# Sprite is a graphic element that can be moved around on the screen. In this code, we will create a simple sprite (a rectangle) that changes color when it touches the boundaries of the window.

import pygame

def main(): # main function to run the game
    pygame.init() # initialize the pygame module
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('color changing sprite')

    # Mapping of color names to RGB values
    colors = { # a dictionary to store color names and their corresponding RGB values using pygame.Color for better readability
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }
    current_color = colors['white'] # initialise the current color to white

    x, y = 30, 30 # initializing the initial position x and y coordinates of the sprite
    sprite_width, sprite_height = 60, 60 # defining the width and height of the sprite

# clock initialization and game loop
    clock = pygame.time.Clock() # initialize a clock object to control the frame rate of the game

    done = False # flag to control the main game loop
    while not done: # main game loop that continues until the user quits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
# Handle key presses to move the sprite and change its color based on boundary contact
        pressed = pygame.key.get_pressed() # retrieve the current state of all keyboard buttons
        if pressed[pygame.K_LEFT]: x -= 3 # if left arrow key is pressed, move the sprite left by decreasing x coordinate, ie if the left arrow key is pressed, decrease the x coordinate by 3 to move the sprite left
        if pressed[pygame.K_RIGHT]: x += 3 #if the right arrow key is pressed, increase the x coordinate by 3 to move the sprite right
        if pressed[pygame.K_UP]: y -= 3 #if the up arrow key is pressed, decrease the y coordinate by 3 to move the sprite up
        if pressed[pygame.K_DOWN]: y += 3 #if the down arrow key is pressed, increase the y coordinate by 3 to move the sprite down
        # Ensure the sprite stays within the screen boundaries
        # Why 3? Because we are moving the sprite by 3 pixels per frame, so we need to ensure that it doesn't go beyond the screen boundaries by more than 3 pixels.

        x = min(max(0, x), screen_width - sprite_width) # Ensure the sprite's x coordinate stays within the left and right boundaries of the screen. The max function ensures that x does not go below 0, and the min function ensures that x does not exceed the right boundary of the screen (screen_width - sprite_width).
        y = min(max(0, y), screen_height - sprite_height) # Ensure the sprite's y coordinate stays within the top and bottom boundaries of the screen. The max function ensures that y does not go below 0, and the min function ensures that y does not exceed the bottom boundary of the screen (screen_height - sprite_height).

        # Change color based on boundary contact
        if x == 0: current_color = colors['blue'] # if sprite is touching the left boundary (x coordinate is 0), change the current color to blue
        elif x == screen_width - sprite_width: current_color = colors['yellow'] # if sprite is touching the right boundary (x coordinate is equal to screen width minus sprite width), change the current color to yellow
        elif y == 0: current_color = colors['red'] # if sprite is touching the top boundary (y coordinate is 0), change the current color to red
        elif y == screen_height - sprite_height:
            current_color = colors['green'] # if sprite is touching the bottom boundary (y coordinate is equal to screen height minus sprite height), change the current color to green
        else:
            current_color = colors['white'] # if sprite is not touching any boundary, keep the current color as white

# Drawing and updating display
        screen.fill((0, 0, 0)) # fill the screen with black color to clear the previous frame before drawing the new frame
        pygame.draw.rect(screen, current_color,
                         (x, y, sprite_width, sprite_height)) # draw a rectangle (the sprite) on the screen with the current color at the position (x, y) with the specified width and height
        pygame.display.flip() # update the display to show the new frame with the drawn sprite
        clock.tick(90) # limit the frame rate to 90 frames per second to ensure smooth movement of the sprite and prevent the game from running too fast

    pygame.quit()


if __name__ == "__main__":
    main()
