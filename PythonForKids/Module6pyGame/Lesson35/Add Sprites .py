# importing pygame module
import pygame

# start pygame
pygame.init()

# screen width and height
w = 600
h = 400

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Add Sprites game")

# basic colors
white = (255, 255, 255)
red = (200, 60, 60)
blue = (60, 60, 200)

# player class for sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y, w, h):
        super().__init__()

        # create rect surface for sprite
        self.image = pygame.Surface((w, h))
        self.image.fill(color)

        # get rect position box
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # mov speed
        self.speed = 5

    def update(self, keys):
        # check keys for moving

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # keep sprite inside screen only

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > w - self.rect.width:
            self.rect.x = w - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > h - self.rect.height:
            self.rect.y = h - self.rect.height


# create 2 sprites
p1 = Player(red, 100, 120, 50, 50)
p2 = Player(blue, 300, 180, 60, 60)

# add sprites in group
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(p2)

running = True
clock = pygame.time.Clock()

# game loop start
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get pressed keys
    keys = pygame.key.get_pressed()

    # only p1 controllable
    p1.update(keys)

    # draw screen
    screen.fill(white)
    all_sprites.draw(screen)

    pygame.display.flip()

# quit game
pygame.quit()