import pygame, random

class Obstacle:
    def __init__(self):
        self.image = pygame.image.load('images/obstacle.png')
        self.trace = (0, 0, 0, 0)
        self.posx, self.posy, self.speed = -210, -999, 0
        self.is_moving = False
    
    def move(self):
        if not self.is_moving:
            self.is_moving = True
            self.posx = random.randint(205, 405)
        else:
            self.posy += self.speed
            if self.posy >= SCREEN_HEIGHT:
                self.posy = -50
                self.is_moving = False
    
    def draw(self):
        self.trace = SCREEN.blit(self.image, (int(self.posx), int(self.posy)))