import pygame
import sys
from background import Background as bg
from game import SCREEN

class Player:
    def __init__(self):
        self.image_straight = pygame.image.load('images/player.png')
        self.image_left = pygame.image.load('images/player_left.png')
        self.image_right = pygame.image.load('images/player_right.png')
        self.image = self.image_straight
        self.trace = (0, 0, 0, 0)
        self.posx, self.posy, self.speed, self.carspeed = 315, 650, 0, -5
        self.moving_left, self.moving_right, self.gas, self.brake = False, False, False, False
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() # exit game if window is closed
                return
            if event.type == pygame.KEYDOWN: # if key pressed down for car movement
                if event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_UP:
                    self.gas = True
                elif event.key == pygame.K_DOWN:
                    self.brake = True
            if event.type == pygame.KEYUP:
                self.moving_left, self.moving_right, self.gas, self.brake = False, False, False, False
        self.image = self.image_straight
        if self.moving_left and not self.posx - 2.5 <= 205:
            self.posx -= 2.5
            self.image = self.image_right
        if self.gas and self.speed < 300:
            self.speed += 1/3
            self.bg.speed  = 0

    def draw(self):
        self.trace = SCREEN.blit(self.image, (int(self.posx), int(self.posy)))
        self.trace = (self.trace[0]+5, self.trace[1]+5, self.trace[2]-10, self.trace[3]-10)