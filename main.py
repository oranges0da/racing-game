from src import Background, Game
import pygame, sys

if __name__ == '__main__':
    bg = Background()
    game = Game()
    game.mainloop()

    pygame.quit()
    sys.quit()