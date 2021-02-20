# Import modules
import pygame

# Functions
def main():
    """ Setup the game display. """
    pygame.init()
    pygame.display.set_mode((640, 240))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    print("quitting")
    pygame.quit()

if __name__ == "__main__":
    main()