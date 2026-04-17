import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("My first game screen")

GREY = (58, 58, 58)

large_image = pygame.image.load("exampleimage.jpg").convert()
large_image = pygame.transform.scale(
    large_image,
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

dog_image = pygame.image.load("dogimage.jpg").convert_alpha()
dog_image = pygame.transform.scale(
    dog_image,
    (300, 300)
)

dog_rect = dog_image.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
)

running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GREY)

    screen.blit(large_image, (0, 0))

    screen.blit(dog_image, dog_rect)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()