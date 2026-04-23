# Write a program to create a Pygame window with two circles, one solid and another hollow circle with border width 3. Keep the background colour as - white RGB(255, 255, 255) and the colour of the rectangle as green (0, 255, 0). Try changing the values of centre and radius to see how the position and size of the balls change.

import pygame

pygame.init()

window=pygame.display.set_mode((350,340))
window.fill((255,255,255))
Green=(0,255,0)
pygame.draw.circle(window,Green,(300,300),50)
pygame.draw.circle(window,Green,(100,100),50,2)
pygame.display.update()
done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False

pygame.quit()