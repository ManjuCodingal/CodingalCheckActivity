# To run code::py -3.10 "C:\Users\vishn\Documents\CodingalCheckActivity\PythonForKids\pyGame\Lsn2\Hollow&SolidBall.py"

import pygame

pygame.init()
# Create the display surface object of specific dimension.
window = pygame.display.set_mode((400, 400))
# Fill the screen with white color
window.fill((255, 255, 255))
# Define colors
GREEN = (0, 255, 0) # green color in RGB format
# Draw solid circle
pygame.draw.circle(window, GREEN, (300, 300), 50)
# Draw outlined circle
pygame.draw.circle(window, GREEN, (100, 100), 50, 3) #(100, 100) is the center of the circle, 50 is the radius and 3 is the thickness of the outline of the circle)
# Draws the surface object to the screen.
pygame.display.update() # updates the display to show the new circles
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Quit pygame
pygame.quit()