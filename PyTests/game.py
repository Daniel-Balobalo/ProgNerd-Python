import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Roaming Bitchass White Box in an 800x600 Plain of Nothingness")

# Character properties
character_width = 50
character_height = 50
character_x = screen_width // 2 - character_width // 2
character_y = screen_height - character_height - 20
character_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all pressed keys
    keys = pygame.key.get_pressed()
    
    # Update character position based on pressed keys
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed
    if keys[pygame.K_UP]:
        character_y -= character_speed
    if keys[pygame.K_DOWN]:
        character_y += character_speed
    
    # Keep the character within the screen boundaries
    character_x = max(0, min(screen_width - character_width, character_x))
    character_y = max(0, min(screen_height - character_height, character_y))
    
    # Clear the screen
    screen.fill(black)
    
    # Draw the character
    pygame.draw.rect(screen, white, (character_x, character_y, character_width, character_height))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Clean up
pygame.quit()
sys.exit()
