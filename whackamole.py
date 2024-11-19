import pygame
import random

def main():
    try:
        pygame.init()

        # Constants
        SCREEN_WIDTH = 640  # Width of game screen
        SCREEN_HEIGHT = 512  # Height of game screen
        GRID_SIZE = 32  # Size of each grid square
        WHITE = (255, 255, 255)  # RGB color for white
        BLACK = (0, 0, 0)  # RGB color for black
        LIGHT_GREEN = (140, 240, 140)  # RGB color for background
        # Load the mole image
        mole_image = pygame.image.load("mole.png")
        # Screen setup
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()
        # Mole position (starts at top-left corner)
        mole_x, mole_y = 0, 0

        # Function to draw grid
        def draw_grid():
            # Draw vertical and horizontal grid lines
            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))

        # Function to move mole to a new random grid position
        def move_mole():
            nonlocal mole_x, mole_y
            # Select new position within the grid boundaries
            mole_x = random.randrange(0, SCREEN_WIDTH // GRID_SIZE) * GRID_SIZE
            mole_y = random.randrange(0, SCREEN_HEIGHT // GRID_SIZE) * GRID_SIZE

        # Start the main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Exit loop if the user closes the window
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if mole is clicked
                    mouse_x, mouse_y = event.pos
                    if (mole_x <= mouse_x < mole_x + GRID_SIZE) and (mole_y <= mouse_y < mole_y + GRID_SIZE):
                        move_mole()  # Move mole if clicked
            # Clear screen
            screen.fill(LIGHT_GREEN)
            # Draw grid and the mole
            draw_grid()
            screen.blit(mole_image, (mole_x, mole_y))
            # Update display
            pygame.display.flip()
            # Cap frame rate at 60 FPS
            clock.tick(60)

    finally:
        pygame.quit()  # Ensure Pygame shuts down properly

if __name__ == "__main__":
    main()
