import pygame
from background import Background
from player import Player
from obstacle import Obstacle

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

bg = Background()
player = Player()
obstacle = Obstacle()

class Game:
    def __init__(self):
        self.score, self.gameover, = 0, False
        self.FONT = pygame.font.Font('../font/Pixeltype.ttf', 20)
    
    def draw_score(self):
        text_speed = self.FONT.render("Speed: " + str(player.speed), True, (255, 255, 255))
        text_score = self.FONT.render("Score: " + str(self.score), True, (255, 255, 255))
        SCREEN.blit(text_speed, (10, 610))
        SCREEN.blit(text_score, (10, 640))
    
    def collision(self):
        p = pygame.Rect(player.trace)
        obs = pygame.Rect(obs.trace)
        cars = [pygame.Rect(car1.trace), pygame.Rect(car2.trace), pygame.Rect(car3.trace)]

        if p.colliderect(obs):
            obs.posx = -50
            self.score += 1
        for car in cars:
            if p.colliderect(car):
                SCREEN.blit(self.image, (int(player.posx - 80), int(player.posy + 10)))
                WINDOW.update()
                pygame.time.delay(5000)
                self.gameover = True
    
    def mainloop(self):
        while not self.gameover:
            clock.tick(FPS)
            bg.draw()
            obstacle.move()
            obstacle.draw()
            player.move()
            player.draw()
            car1.move()
            car1.draw()
            car2.move()
            car2.draw()
            car3.move()
            car3.draw()
            self.draw_score()
            self.collision()
            WINDOW.update()