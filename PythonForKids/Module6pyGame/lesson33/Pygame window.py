# Write a Python program to create an empty Pygame window.

import pygame

pygame.init()
pygame.display.set_caption("PyGame Window")
screen=pygame.display.set_mode((300,200))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            done=True
    # screen.fill((255,255,255))
    screen.fill(pygame.Color("red"))
    pygame.display.flip()

        
        
