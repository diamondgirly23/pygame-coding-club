import pygame
import math
import random
pygame.init()
pygame.font.init()
#how to make a font?

screen = pygame.display.set_mode((1280,720))
#This object is for making game run smoother
clock = pygame.time.Clock()
running = True
dt = 0
ball_posx = pygame.display.get_window_size()[0]/2
ball_posy = pygame.display.get_window_size()[1]/2
ball_changex = random.randint(4,5)
ball_changey = random.randint(1,3)
player1y = pygame.display.get_window_size()[1]/2
player2y = pygame.display.get_window_size()[1]/2
player1x = 30
player2x = 1220
player1y_change = 0
player2y_change = 0

player1win = False
player2win = False
player1points = 0
player2points = 0
def moveBall(ballx,bally,ballx_change,bally_change):
    
    pass

def movePlayer(playery,playery_change):
    pass

def ballWallCollision(ballx,bally):
    pass

def playerCollision(playerx,playery,ballx,bally):
    pass

def reset(ballx,bally,ball_changex,ball_changey):
    pass
def checkwin(ballx,bally):
    pass

def victoryScreen(player):
    pass

while running:
    pass
