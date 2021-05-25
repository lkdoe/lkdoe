import pygame
import sys

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)



def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
    screen.fill((150, 200, 150))

    # Drawing a test rectangle onto the screen
    rect = pygame.Rect(20, 20, 30, 30)
    pygame.draw.rect(screen, "black", rect)
    pygame.draw.circle(screen, "red", (200, 50), 30, 10)

    
    while True:
        clock.tick(10)
        # Other stuff goes here. ;-)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
    pass


if __name__ == "__main__":
    main()
