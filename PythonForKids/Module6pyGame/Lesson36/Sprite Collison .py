# 1) Import required modules:
#    a) Import `pygame` to create the game window, sprites, and handle events.
#    b) Import `random` to place sprites at random positions.
import pygame
import random

# 2) Create constants for easy changes:
#    a) `SCREEN_WIDTH`, `SCREEN_HEIGHT` for window size.
#    b) `MOVEMENT_SPEED` for how fast the sprite moves.
#    c) `FONT_SIZE` for the win message size.
SCREEN_WIDTH=600
SCREEN_HEIGHT=500
FONT_SIZE=40
MOVEMENT_SPEED=5

# 3) Initialize pygame using `pygame.init()`.
pygame.init()

# 4) Load the background image `bg.jpg` and scale it to fit the screen size
#    using `pygame.transform.scale(...)`.
background_img=pygame.image.load("example.jpg")
background_img=pygame.transform.scale(background_img,(SCREEN_WIDTH,SCREEN_HEIGHT))

# 5) Load the font once using `pygame.font.SysFont("Times New Roman", FONT_SIZE)`.
font=pygame.font.SysFont("Times New Roman", FONT_SIZE)

# 6) Create a class `Sprite` that inherits from `pygame.sprite.Sprite`.
class sprite(pygame.sprite.Sprite):


# 7) Define the constructor `__init__(self, color, height, width)`:
#    a) Call the parent constructor using `super().__init__()`.
#    b) Create a surface for the sprite using `pygame.Surface([width, height])`.
#    c) Fill the sprite background with "dodgerblue".
#    d) Draw a rectangle of the given `color` on top of the sprite surface.
#    e) Create a rectangle (`self.rect`) to store the sprite’s position using `get_rect()`.
    def __init__(self,color,height,width):
        super().__init__()
        
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.rect=self.image.get_rect()

# 8) Define a method `move(self, x_change, y_change)`:
#    a) Update `self.rect.x` by adding `x_change`.
#    b) Update `self.rect.y` by adding `y_change`.
#    c) Clamp the sprite inside the screen boundaries so it cannot move outside the window.
    def move(self, x_change, y_change):
        self.rect.x+=x_change
        self.rect.y+=y_change
        if self.rect.x<0:
            self.rect.x=0
        if self.rect.y<0:
            self.rect.y=0
        if self.rect.right>SCREEN_WIDTH:
            self.rect.right=SCREEN_WIDTH
        if self.rect.bottom>SCREEN_HEIGHT:
            self.rect.bottom=SCREEN_HEIGHT

# 9) Create the game window using `pygame.display.set_mode(...)`
#    and set the title to "Sprite Collision".
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collison")

# 10) Create a sprite group `all_sprites = pygame.sprite.Group()` to store and draw sprites.
all_sprites=pygame.sprite.Group()

# 11) Create `sprite1` (black sprite):
#     a) Create the sprite with size 20x30.
#     b) Set its starting position randomly inside the screen.
#     c) Add it to `all_sprites`.
sprite1=sprite("black",20,30)
sprite1.rect.x=random.randint(0,SCREEN_WIDTH-20)
sprite1.rect.y=random.randint(0,SCREEN_HEIGHT-30)
all_sprites.add(sprite1)

# 12) Create `sprite2` (red sprite):
#     a) Create the sprite with size 20x30.
#     b) Set its starting position randomly inside the screen.
#     c) Add it to `all_sprites`.
sprite2=sprite("red",20,30)
sprite2.rect.x=random.randint(0,SCREEN_WIDTH-20)
sprite2.rect.y=random.randint(0,SCREEN_HEIGHT-30)
all_sprites.add(sprite2)


# 13) Initialize game control variables:
#     a) `running = True` to keep the game loop running.
#     b) `won = False` to track if the player has won.
#     c) Create a `clock` object using `pygame.time.Clock()` to control FPS.
running=True
won=False
clock=pygame.time.Clock()


# 14) Start the main game loop `while running`:


# 15) Handle events:
#     a) If the user closes the window (`pygame.QUIT`), stop the loop.
#     b) If the user presses the 'X' key, stop the loop.
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                running=False

# 16) If the game is not won yet (`if not won`):
#     a) Detect arrow key presses using `pygame.key.get_pressed()`.
#     b) Calculate `x_change` and `y_change` based on key presses and speed.
#     c) Move `sprite1` using `sprite1.move(x_change, y_change)`.
    if not won:
        keys=pygame.key.get_pressed()
        x_change=0
        y_change=0
        if keys[pygame.K_LEFT]:
            x_change=-MOVEMENT_SPEED
        if keys[pygame.K_RIGHT]:
            x_change=MOVEMENT_SPEED
        if keys[pygame.K_UP]:
            y_change=-MOVEMENT_SPEED
        if keys[pygame.K_DOWN]:
            y_change=MOVEMENT_SPEED
        sprite1.move(x_change,y_change)
        
        
        
        
        

# 17) Check collision between `sprite1` and `sprite2` using `colliderect()`:
#     a) If they collide, remove `sprite2` from the sprite group.
#     b) Set `won = True`.
    if sprite1.rect.colliderect(sprite2.rect):
        sprite2.kill
        won=True

# 18) Draw everything:
#     a) Draw the background image using `screen.blit(background_image, (0, 0))`.
#     b) Draw all sprites using `all_sprites.draw(screen)`.
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)


# 19) If the player has won:
#     a) Render the text "You win!" using the font.
#     b) Display the text at the center of the screen using `blit`.
    if won:
        text=font.render("You Win!",True,(0,0,0))
        text_rect=text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
        screen.blit(text,text_rect)

# 20) Update the screen using `pygame.display.flip()`.
    pygame.display.flip()


# 21) Limit the frame rate to 90 FPS using `clock.tick(90)`.
    clock.tick(90)

# 22) When the game loop ends, close pygame using `pygame.quit()`.
pygame.quit()