import pygame
from background import Background
from player import Player

# basic pygame setup
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT, FPS = 700, 800, 120
WINDOW = pygame.display
WINDOW.set_caption("Racing Game")
SCREEN = WINDOW.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = Background(SCREEN)
player = Player(bg)

class Game():
    def __init__(self):
        pass