import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('color changing sprite')

    # Mapping of color names to RGB values
    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }
    current_color = colors['white']

    x, y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        # Change color based on boundary contact
        if x == 0: current_color = colors['blue']
        elif x == screen_width - sprite_width: current_color = colors['yellow']
        elif y == 0: current_color = colors['red']
        elif y == screen_height - sprite_height:
            current_color = colors['green']
        else:
            current_color = colors['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,
                         (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()


if __name__ == "__main__":
    main()




# Write a program that detects when keys are pressed and changes the color of a sprite when it touches the screen boundaries.
# # 1) Import the `pygame` library to create a window, handle keyboard input, and draw shapes.
# import pygame

# # 2) Define a function `main()` to contain the full game logic.
# def main():

# # 3) Inside `main()`:
# #    a) Initialize pygame using `pygame.init()`.
#         pygame.init()
# #    b) Set screen dimensions (`screen_width`, `screen_height`) to 500x500.
#         screen_width=400
#         screen_height=500
# #    c) Create the game window using `pygame.display.set_mode(...)`.
#         screen=pygame.display.set_mode((screen_width,screen_height))
# #    d) Set the window title using `pygame.display.set_caption(...)`.
#         pygame.display.set_caption("Colour Chnaging Sprite")

# # 4) Create a dictionary `colors` to map color names to RGB values using `pygame.Color(...)`.
#         colors={
#                 'white':pygame.Color('white'),
#                 'blue':pygame.Color('blue'),
#                 'red':pygame.Color('red'),
#                 'yellow':pygame.Color('yellow'),
#                 'green':pygame.Color('green')
#         }

# # 5) Set the initial sprite color to white using:
# #    `current_color = colors['white']`.
#         current_color=colors['white']

# # 6) Set the starting position of the sprite:
# #    a) `x, y = 30, 30`
#         x,y=30,30
     

# # 7) Set the sprite size:
# #    a) `sprite_width, sprite_height = 60, 60`
#         sprite_width=60
#         sprite_height=60

# # 8) Create a clock object using `pygame.time.Clock()` to control the frame rate.
#         clock=pygame.time.Clock()

# # 9) Create a loop control variable `done = False`.
#         done=False

# # 10) Start the main game loop `while not done`:
# #     a) Handle events using `pygame.event.get()`.
# #     b) If the event is `pygame.QUIT`, set `done = True` to exit the loop.
#         while not done:
#                 for event in pygame.event.get():
#                         if event.type==pygame.QUIT:
#                                 done=True

# # 11) Read keyboard inputs using `pygame.key.get_pressed()`:
# #     a) If LEFT key is pressed, move sprite left by decreasing `x`.
# #     b) If RIGHT key is pressed, move sprite right by increasing `x`.
# #     c) If UP key is pressed, move sprite up by decreasing `y`.
# #     d) If DOWN key is pressed, move sprite down by increasing `y`.
                
#                 keys=pygame.key.get_pressed()
#                 if keys[pygame.K_LEFT]:
#                         x-=5
#                 if keys[pygame.K_RIGHT]:
#                         x+=5
#                 if keys[pygame.K_UP]:
#                         y-=5
#                 if keys[pygame.K_DOWN]:
#                         y+=5

# # 12) Restrict the sprite to stay inside the screen boundaries:
# #     a) Clamp `x` between 0 and `screen_width - sprite_width`.
# #     b) Clamp `y` between 0 and `screen_height - sprite_height`.
#                 x=max(0,min(x,screen_width,screen_height))
#                 y=max(0,min(y,screen_height,screen_width))

# # 13) Change the sprite color based on which boundary it touches:
# #     a) If `x == 0`, change to blue (left wall).
# #     b) Else if `x == screen_width - sprite_width`, change to yellow (right wall).
# #     c) Else if `y == 0`, change to red (top wall).
# #     d) Else if `y == screen_height - sprite_height`, change to green (bottom wall).
# #     e) Otherwise, keep it white (not touching any boundary).
#                 if x==0:
#                         current_color=colors['blue']
#                 elif x==screen_width-sprite_width:
#                         current_color=colors['yellow']
#                 elif y==0:
#                         current_color=colors['red']
#                 elif y==screen_height-sprite_width:
#                         current_color=colors['green']
#                 else:
#                         current_color=colors['white']

# # 14) Draw everything on the screen:
# #     a) Fill the background with black using `screen.fill((0, 0, 0))`.
# #     b) Draw the sprite as a rectangle using `pygame.draw.rect(...)`.
#                 screen.fill((0,0,0))
#                 pygame.draw.rect(screen,current_color,(x,y,sprite_width,sprite_height))

# # 15) Update the display using `pygame.display.flip()`.
#                 pygame.display.flip()

# # 16) Limit the frame rate using `clock.tick(90)`.
#                 clock.tick(90)

              

# # 17) After the loop ends, close pygame using `pygame.quit()`.
#         pygame.quit()

# # 18) Use `if __name__ == "__main__":` to call `main()` only when
# #     the file is run directly.
# if __name__=="__main__":
#         main()



