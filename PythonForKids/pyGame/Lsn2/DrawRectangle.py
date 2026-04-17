# To run code:: py -3.10 "C:\Users\vishn\Documents\CodingalCheckActivity\PythonForKids\pyGame\Lsn2\DrawRectangle.py" 

import pygame  
  
pygame.init()  # initialize pygame module
screen = pygame.display.set_mode((400, 300))  # W and H of the window
done = False  # flag to control the main loop
  
while not done:  
    for event in pygame.event.get():  # iterates over all events in the event queue
        if event.type == pygame.QUIT:  
            done = True  
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))    # rgb color and rectangle dimensions 60*60 at (30, 30) coordinates
  
    pygame.display.flip()   # updates the display to show the new rectangle