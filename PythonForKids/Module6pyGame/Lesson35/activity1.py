# To run code::py -3.10 "C:\Users\vishn\Documents\CodingalCheckActivity\PythonForKids\module6pyGame\Lesson35\activity1.py"
# Boundary Sprite: A sprite that changes color when it hits the boundary of the window. The background color also changes when the sprite hits the boundary.
import pygame
import random

# Initialize Pygame
pygame.init()

# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1 # Custom event for changing the sprite's color. The value is set to pygame.USEREVENT + 1 to ensure it does not conflict with any existing Pygame events. +1 is added to create a unique event ID for the sprite color change event. means that when this event is posted, it will trigger the logic to change the sprite's color in the game loop.
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2 # Custom event for changing the background color. The value is set to pygame.USEREVENT + 2 to ensure it does not conflict with any existing Pygame events. +2 is added to create a unique event ID for the background color change event. means that when this event is posted, it will trigger the logic to change the background color in the game loop. instead of +2 we can also use +1 for the background color change event as well, but using +2 helps to keep the event IDs organized and distinct, making it easier to manage and understand the different events in the game.

# Define basic colors using pygame.Color
# Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')


# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite): # The Sprite class inherits from pygame.sprite.Sprite, which is a base class provided by Pygame for creating game objects. By inheriting from this class, we can take advantage of built-in functionality for managing sprites, such as grouping and collision detection. This allows us to create a sprite that can move around the screen and interact with the boundaries, changing colors when it hits them.

  # Constructor method. Initializes the sprite's properties such as color, size, and velocity.
  def __init__(self, color, height, width):
    # Call to the parent class (Sprite) constructor
    super().__init__()
    # Create the sprite's surface with dimensions and color
    self.image = pygame.Surface([width, height]) # Creates a new Surface object for the sprite with the specified width and height. By creating this surface, we can later fill it with a color and use it to display the sprite on the screen.
    self.image.fill(color)
    # Get the sprite's rect defining its position and size
    self.rect = self.image.get_rect() # The rect attribute is a Pygame Rect object that defines the position and size of the sprite. It is used for positioning the sprite on the screen and for collision detection. The get_rect() method creates a Rect object that matches the dimensions of the sprite's image, allowing us to easily manage its position and detect when it hits the boundaries of the window.
    # Set initial velocity with random direction
    self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])] # The velocity attribute is a list that represents the speed and direction of the sprite's movement. The random.choice([-1, 1]) function randomly selects either -1 or 1 for both the x and y components of the velocity, which means the sprite can move in any of the four diagonal directions (up-left, up-right, down-left, down-right) when it starts. This adds an element of unpredictability to the sprite's movement as it bounces around the screen.

  # Method to update the sprite's position
  def update(self):
    # Move the sprite by its velocity
    self.rect.move_ip(self.velocity) # ip stands for move in place. This method updates the position of the sprite by adding the velocity values to the current position defined by the rect. The move_ip() method modifies the rect's position directly, allowing the sprite to move smoothly across the screen based on its velocity.
    # Flag to track if the sprite hits a boundary
    boundary_hit = False
    # Check for collision with left or right boundaries and reverse direction
    if self.rect.left <= 0 or self.rect.right >= 500: # <) Checks if the sprite's left edge has hit the left boundary (0) or if the right edge has hit the right boundary (500). If either condition is true, it means the sprite has collided with a horizontal boundary.
      self.velocity[0] = -self.velocity[0] # Reverses the horizontal component of the sprite's velocity by negating its value. This causes the sprite to change direction and move in the opposite horizontal direction when it hits a boundary. 0 is used to access the horizontal component of the velocity list, which represents the speed and direction of movement along the x-axis. By negating this value, we effectively reverse the sprite's horizontal movement direction.
      boundary_hit = True
    # Check for collision with top or bottom boundaries and reverse direction
    if self.rect.top <= 0 or self.rect.bottom >= 400: # Checks if the sprite's top edge has hit the top boundary (0) or if the bottom edge has hit the bottom boundary (400). If either condition is true, it means the sprite has collided with a vertical boundary.
      self.velocity[1] = -self.velocity[1] # Reverses the vertical component of the sprite's velocity by negating its value. This causes the sprite to change direction and move in the opposite vertical direction when it hits a boundary. 1 is used to access the vertical component of the velocity list, which represents the speed and direction of movement along the y-axis. By negating this value, we effectively reverse the sprite's vertical movement direction.
      boundary_hit = True

    # If a boundary was hit, post events to change colors
    if boundary_hit:
      pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT)) # SPRITE_COLOR_CHANGE_EVENT is a custom event that we defined earlier to indicate that the sprite's color should change. When the sprite hits a boundary, this line creates a new Pygame event with the type SPRITE_COLOR_CHANGE_EVENT and posts it to the event queue. This allows the game loop to detect when the sprite has hit a boundary and trigger the logic to change the sprite's color accordingly.
    #   When the sprite hits a boundary, this line creates a new Pygame event with the type SPRITE_COLOR_CHANGE_EVENT and posts it to the event queue. This allows the game loop to detect when the sprite has hit a boundary and trigger the logic to change the sprite's color accordingly.
      pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT)) # When the sprite hits a boundary, this line creates a new Pygame event with the type BACKGROUND_COLOR_CHANGE_EVENT and posts it to the event queue. This allows the game loop to detect when the sprite has hit a boundary and trigger the logic to change the background color accordingly.

  # Method to change the sprite's color
  def change_color(self):
    self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))


# Function to change the background color
def change_background_color():
  global bg_color
  bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])


# Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group() # Groups in Pygame are used to manage multiple sprites together. By creating a sprite group, we can easily update and draw all the sprites in the group with a single call. This simplifies the game loop and allows for better organization of our game objects. In this case, we create a group called all_sprites_list to hold our sprite(s) and manage their updates and rendering efficiently. Multiple sprites concept comes as it hit boundary and changes color, we can add more sprites to the group and they will all be updated and drawn together in the game loop without needing to manage each sprite individually.
# A sprite group is a collection of sprites that can be managed together. By adding our sprite to a group, we can easily update and draw all the sprites in the group with a single call. This simplifies the game loop and allows for better organization of our game objects.
# Instantiate the sprite
sp1 = Sprite(WHITE, 20, 30) # Creates an instance of the Sprite class with a white color, height of 20 pixels, and width of 30 pixels. This initializes the sprite's properties and prepares it for use in the game. The sprite will start with a random velocity and will be positioned randomly on the screen when we set its rect.x and rect.y values.
# Randomly position the sprite
sp1.rect.x = random.randint(0, 480) # Sets the x-coordinate of the sprite's rectangle to a random value between 0 and 480.
sp1.rect.y = random.randint(0, 370) # Sets the y-coordinate of the sprite's rectangle to a random value between 0 and 370.
# Add the sprite to the group
all_sprites_list.add(sp1) # Adds the sprite instance (sp1) to the all_sprites_list group. This allows us to manage and update the sprite along with any other sprites that may be added to the group in the future. By adding the sprite to the group, we can easily call update() and draw() methods on the entire group, which simplifies our game loop and keeps our code organized.

# Create the game window
screen = pygame.display.set_mode((500, 400))
# Set the window title
pygame.display.set_caption("Boundary Sprite")
# Set the initial background color
bg_color = BLUE
# Apply the background color
screen.fill(bg_color)

# Game loop control flag
exit = False
# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Main game loop
while not exit:
  # Event handling loop
  for event in pygame.event.get():
    # If the window's close button is clicked, exit the game
    if event.type == pygame.QUIT:
      exit = True
    # If the sprite color change event is triggered, change the sprite's color
    elif event.type == SPRITE_COLOR_CHANGE_EVENT:
      sp1.change_color()
    # If the background color change event is triggered, change the background color
    elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
      change_background_color()

  # Update all sprites
  all_sprites_list.update() # Calls the update() method for all sprites in the all_sprites_list group. This will move the sprite according to its velocity and check for boundary collisions, which may trigger color change events if a collision occurs.

  # Fill the screen with the current background color
  screen.fill(bg_color)
  # Draw all sprites to the screen
  all_sprites_list.draw(screen) # Draws all the sprites in the all_sprites_list group onto the screen. This method iterates through each sprite in the group and blits its image onto the screen at the position defined by its rect. This is necessary to visually update the sprite's position and color changes on the screen after each update cycle.

  # Refresh the display
  pygame.display.flip()
  # Limit the frame rate to 240 fps
  clock.tick(240) # The clock.tick(240) method limits the game loop to run at a maximum of 240 frames per second (fps). This helps to ensure that the game runs smoothly and does not consume excessive CPU resources. By controlling the frame rate, we can maintain consistent performance and prevent the game from running too fast on powerful hardware or too slow on less capable machines.

# Uninitialize all pygame modules and close the window
pygame.quit()
