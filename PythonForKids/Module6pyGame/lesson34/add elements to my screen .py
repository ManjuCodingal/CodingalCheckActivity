import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("My first game screen")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

rect_width = 120
rect_height = 80

rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2

rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

font = pygame.font.Font(None, 36)

text = font.render("Hello Pygame!", True, BLACK)

text_rect = text.get_rect(center=(320, 50))

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, rectangle)

    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()