import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_WIDTH))

clock = pygame.time.Clock()


def main_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
        clock.tick()

        display_surface.fill((0,0,0))

        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    main_loop()