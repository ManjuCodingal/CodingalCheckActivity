# # 1) Import the `pygame` library to create a window, load images, and display text.

import pygame

# 2) Initialize pygame using `pygame.init()`.

pygame.init()

# 3) Set screen width and height using:
#    `SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500`.

SCREEN_WIDTH,SCREEN_HEIGHT=500,500

# 4) Create the game window (display surface) using `pygame.display.set_mode(...)`

#    and set the window title using `pygame.display.set_caption(...)`.

SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Python game")

# 5) Load and scale the background image:
#    a) Load the image file `background.png`.
background=pygame.transform.scale(pygame.image.load("example.jpg").convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))
#    b) Use `.convert()` for faster display.

#    c) Scale it to fit the window size `(SCREEN_WIDTH, SCREEN_HEIGHT)`.


# 6) Load and scale the penguin image:
#    a) Load `penguin.png`.
dog=pygame.transform.scale(pygame.image.load("dogimage.jpg").convert_alpha(),(200,200))
#    b) Use `.convert_alpha()` to keep transparency.
#    c) Scale it to size (200, 200).

# 7) Create a rectangle (`penguin_rect`) for positioning the penguin:
dog_rect=dog.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
#    a) Use `get_rect(center=(...))` to place it near the center of the screen.

# 8) Create and display text on the screen:
#    a) Create a font object using `pygame.font.Font(None, 36)`.
font=pygame.font.Font(None,36)
#    b) Render the text "Hello World" with black color.
text=font.render("Hello World",True, pygame.Color('black'))

#    c) Get a rectangle (`text_rect`) and set its center position.
text_rect=text.get_rect(center=(SCREEN_WIDTH//2,50))
# 9) Define the main game function `game_loop()`:
#    a) Create a clock object using `pygame.time.Clock()` to control FPS.
clock=pygame.time.Clock()
def game_loop():
    running=True
#    b) Set `running = True` to control the loop.

# 10) Start the main game loop `while running`:
    while running:
#     a) Use `pygame.event.get()` to check events.
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
#     b) If the user clicks the close button (`pygame.QUIT`), set `running = False`.

# 11) Draw all elements on the screen in order:
#     a) Draw the background image at (0, 0) using `blit`.
        SCREEN.blit(background,(0,0))
#     b) Draw the penguin image at `penguin_rect`.
        SCREEN.blit(dog,dog_rect)
#     c) Draw the text at `text_rect`.
        SCREEN.blit(text,text_rect)

# 12) Update the display using `pygame.display.flip()`
#     so the drawn elements become visible.
        pygame.display.flip()

# 13) Limit the frame rate to 30 FPS using `clock.tick(30)`.
        clock.tick(30)

# 14) When the loop ends, quit pygame using `pygame.quit()`.
    pygame.quit

# 15) Use `if __name__ == '__main__':` to run `game_loop()` only when
if __name__=="__main__":

    game_loop()
#     this file is executed directly.