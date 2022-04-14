import pygame

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
        if