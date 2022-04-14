from src import Game
import pygame, sys

if __name__ == '__main__':
    game = Game()
    game.mainloop()

    pygame.quit()
    sys.quit()