import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    pygame.init()

    #set up screen
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #set up clock
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update the player
        player.update(dt)
        
        # Fill screen with black
        screen.fill("black")
        # Re-render the player
        player.draw(screen)
        # Update the display
        pygame.display.flip()

        # Update the clock and limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()