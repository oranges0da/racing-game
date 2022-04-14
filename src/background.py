import pygame
from game import SCREEN

class Background:
    def __init__(self):
        self.bg = pygame.image.load('../images/bg.jpeg').convert_alpha()
        self.posy = self.speed = -700, 0

    def draw(self):
        self.posy += self.speed
        if self.posy >= 0:
            self.posy = -700

        SCREEN.blit(self.bg, (0, int(self.posy)))