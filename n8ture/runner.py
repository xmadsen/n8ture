# Simple pygame program

# Import and initialize the pygame library
import pygame


class Runner:
    def __init__(self, SCREEN_WIDTH=800, SCREEN_HEIGHT=800):
        pygame.init()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

    def start(self):
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])

        # Run until the user asks to quit
        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the background with white
            self.screen.fill((255, 255, 255))

            self.draw_grid()

        # Done! Time to quit.
        pygame.quit()

    def draw_grid(self, grid_divisions=10):
        grid_surf = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        even_color = (209, 211, 196)
        odd_color = (223, 224, 220)

        for i in range(grid_divisions):
            for j in range(grid_divisions):
                color = even_color if (i + j) % 2 == 0 else odd_color
                pygame.draw.rect(
                    grid_surf,
                    color,
                    pygame.Rect(
                        i * (self.SCREEN_WIDTH // grid_divisions),
                        j * (self.SCREEN_HEIGHT // grid_divisions),
                        self.SCREEN_WIDTH // grid_divisions,
                        self.SCREEN_HEIGHT // grid_divisions,
                    ),
                )

        surf_center = (
            (self.SCREEN_WIDTH - grid_surf.get_width()) / 2,
            (self.SCREEN_HEIGHT - grid_surf.get_height()) / 2,
        )
        self.screen.blit(grid_surf, surf_center)
        # Flip the display
        pygame.display.flip()
