import pygame, random

from src import player

class Car:
    def __init__(self, posx):
        self.image0 = pygame.image.load('images/car1.png')
        self.image1 = pygame.image.load('images/car2.png')
        self.image2 = pygame.image.load('images/car3.png')
        self.image_list = (self.image0, self.iamge1, self.image2)
        self.trace = (0, 0, 0, 0)
        self.posx, self.posy, self.speed = posx, -500, 0
        self.is_moving = False
    
    def move(self):
        if not self.is_moving:
            rnd = random.randint(1, 100)
            if rnd == 50:
                self.is_moving = True
                self.speed = random.randint(1, 3)
        else:
            self.posy += self.speed
            if self.posy >= SCREEN_HEIGHT and player.speed > 200:
                self.posy = -500
                self.is_moving = False
    
    def draw(self):
        self.trace = SCREEN.blit(self.image, (int(self.posx), int(self.posy)))
        self.trace = (self.trace[0]+5, self.trace[1]+5, self.trace[2]-10, self.trace[3]-10)
        