import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event: Sprite Color Change")

# Colors
WHITE = (255, 255, 255)

# Custom event (trigger every 1 second)
COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 1000)

# Sprite class
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.color = self.random_color()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def random_color(self):
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))

    def change_color(self):
        self.color = self.random_color()
        self.image.fill(self.color)

# Create sprites
sprite1 = ColorSprite(100, 150)
sprite2 = ColorSprite(350, 150)

# Sprite group
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Custom event triggers color change
        if event.type == COLOR_CHANGE_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Draw sprites
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()