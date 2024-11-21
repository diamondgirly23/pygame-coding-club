import pygame
import math
import random
pygame.init()
pygame.font.init()
#how to make a font?


#if you change the dimensions of the window remember that it will impact where the placement of things are and you must adjust accordingly
screen = pygame.display.set_mode((1280,720))
#This object is for making game run smoother
clock = pygame.time.Clock()
dt = 0
#this is for the while loop
running = True

#This is one way of doing it, I think there is a .getwidth and a ,getheight method you can  try out as well.
#This way you have to choose the first index for x and second index for y sin the value it returns is a 2 size array.
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

#Hint, this is straight forward dont overthink things, also second hint, return ballx,bally at the end
#Dont forget in python you can return multiple things at once. you just need to make it be like
# x,y = moveBall() (this is where you call the function)
#where x,y will be the variables that you have your return feed into.
def moveBall(ballx,bally,ballx_change,bally_change):
    
    pass


#hint this function can be used with both players interchangibly (think about how to achieve this)
def movePlayer(playery,playery_change):
    pass

#hint, what will you return? what is changing when the ball hits the wall.
def ballWallCollision(ballx,bally, ballx_change, bally_change):
    pass
#hint, Think about what you are returning.
#What are you checking for? 
def playerWallCollision(playery):
    pass
#Hint, dont get overwhelmed by the amount of parameters in it, just think about each part separately and how it fits together.
#What is ultimately the goal of this function?
def playerBallCollision(playerx,playery,ballx,bally,ballx_change,bally_change):
    pass

#no parameters. Hint though, it will need to return at least 4 different values. Think about what its going to do.
def reset():
    pass
#This will check if the ball is past either paddle (hint you need to be able to differentiate between which side gets the point)
def checkwin(ballx,bally):
    pass


#hint there needs to be a while loop inside of this function so it wont go back to the main game loop
def victoryScreen(player):
    pass



#This will be where you make the main game loop.
while running:
    pass

