import pygame
import random


def main():
    try:
        pygame.init()

        # Constants
        SCREEN_WIDTH = 640
        SCREEN_HEIGHT = 512
        GRID_SIZE = 32
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        LIGHT_GREEN = (144, 238, 144)

        # Load the mole image
        mole_image = pygame.image.load("mole.png")

        # Screen setup
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()

        # Mole position (starts at top-left corner)
        mole_x, mole_y = 0, 0

        # Function to draw the grid
        def draw_grid():
            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))

        # Function to move the mole to a new random grid position
        def move_mole():
            nonlocal mole_x, mole_y
            mole_x = random.randrange(0, SCREEN_WIDTH // GRID_SIZE) * GRID_SIZE
            mole_y = random.randrange(0, SCREEN_HEIGHT // GRID_SIZE) * GRID_SIZE

        # Start the main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mole is clicked
                    mouse_x, mouse_y = event.pos
                    if (mole_x <= mouse_x < mole_x + GRID_SIZE) and (mole_y <= mouse_y < mole_y + GRID_SIZE):
                        move_mole()

            # Clear the screen
            screen.fill(LIGHT_GREEN)

            # Draw the grid and the mole
            draw_grid()
            screen.blit(mole_image, (mole_x, mole_y))

            # Update the display
            pygame.display.flip()

            # Cap the frame rate at 60 FPS
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
