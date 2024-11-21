import pygame
import math
import random
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pong")
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
def victoryscreen(player, screen):
    
    while running:
        screen.fill("black")
        newscreen = my_font.render(player + " Wins!",False,"White")
        screen.blit(newscreen,(pygame.display.get_window_size()[0]/2,pygame.display.get_window_size()[1]/2))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
        
        #If the event is pressing the quit button then the game will quit out by making running false.
           if event.type == pygame.QUIT:
            running = False
            continue


def reset():
    ball_posx = pygame.display.get_window_size()[0]/2
    ball_posy = pygame.display.get_window_size()[1]/2
    ball_changex = random.randint(4,5)
    ball_changey = random.randint(1,3)
    return ball_posx,ball_posy,ball_changex,ball_changey

def playerCollision(ballx,bally,playery, playerx, ballxchange):
    
    
    if (bally < playery+150 and bally > playery) and (ballx > playerx-15 and ballx < playerx+30):
       
       if ballxchange < 0 and playerx == 30:
            ballxchange *= -1.05
       if ballxchange > 0 and playerx == 1220:
            ballxchange *= -1.05

    return ballxchange

def player_WallCollision(playery):
    if playery > pygame.display.get_window_size()[1]-150:
        playery = pygame.display.get_window_size()[1]-150
    elif playery < 0:
        playery = 0
    return playery

def ball_WallCollision(x,y,changex,changey,player1win,player2win):
    if x > pygame.display.get_window_size()[0]:
        player1win = True
    elif x < 0:
        player2win = True
    if y > pygame.display.get_window_size()[1]-15:
        changey*= -1
    if y < 15:
        changey*= -1


    return changex,changey,player1win,player2win



    
def moveBall(x,y, ball_changex,ball_changey):
    x += ball_changex
    y +=ball_changey
    return x,y

def player1move(ychange, player1y):
    player1y += ychange
    return player1y
def player2move(ychange, player2y):
    player2y += ychange
    return player2y

    
while running:
    # In pygame there is a event system where everything that happens (like the user pressing a key) is logged in the event queue
    #We are using a for loop to loop through each event that is in the log and checking which event it is.
    for event in pygame.event.get():
        
        #If the event is pressing the quit button then the game will quit out by making running false.
        if event.type == pygame.QUIT:
            running = False
            continue
        #pygame.KEYDOWN is a event that triggers when the user first presses a key.
        if event.type == pygame.KEYDOWN:
            #After the keydown event is triggered we now check to see WHICH key got pressed.
            if event.key == pygame.K_UP:
               player2y_change -=3
            elif event.key == pygame.K_DOWN:
               player2y_change +=3
            if event.key == pygame.K_w:
               player1y_change -=3
            elif event.key == pygame.K_s:
               player1y_change +=3
        #pygame.KEYUP is a event that triggers when the user stops pressing a key .
        if event.type == pygame.KEYUP:
            #after the user lets go of the key and triggers the event we now need to check which key was let go of.
            if event.key == pygame.K_UP:
               player2y_change +=3
            elif event.key == pygame.K_DOWN:
                player2y_change -=3
            if event.key == pygame.K_w:
               player1y_change +=3
            elif event.key == pygame.K_s:
                player1y_change -=3


    #this fills the screen with black 
    screen.fill("black")


    #This moves the ball.
    ball_posx,ball_posy = moveBall(ball_posx,ball_posy,ball_changex,ball_changey)

    #This checks for ball wall collision
    ball_changex, ball_changey,player1win,player2win = ball_WallCollision(ball_posx,ball_posy,ball_changex,ball_changey,player1win,player2win)

    #players will move now.
    player1y = player1move(player1y_change, player1y)
    player2y = player2move(player2y_change, player2y)
    
    #Check for player wall collision
    player1y = player_WallCollision(player1y)
    player2y = player_WallCollision(player2y)
    #Check for player collision
    ball_changex = playerCollision(ball_posx,ball_posy,player1y,player1x,ball_changex)
    ball_changex = playerCollision(ball_posx,ball_posy,player2y,player2x,ball_changex)
   
   #This puts the score on the screen.
    newscreen = my_font.render(str(player1points),False,"White")
    screen.blit(newscreen,(pygame.display.get_window_size()[0]/2-40,30))
    newscreen = my_font.render(str(player2points),False,"White")
    screen.blit(newscreen,(pygame.display.get_window_size()[0]/2+40,30))
     #This checks if ball is past the goal.
    if player1win:
        player1points +=1
        ball_posx,ball_posy,ball_changex,ball_changey = reset()
        player1win = False
    elif player2win:
        player2points +=1
        ball_posx,ball_posy,ball_changex,ball_changey = reset()
        player2win = False
    if player1points > 6:
        victoryscreen("Player 1",screen)
    if player2points > 6:
        victoryscreen("Player 2",screen)

     #This draws the ball at the current location.
    pygame.draw.circle(screen, "red",(ball_posx,ball_posy), 15)

    #draws player 1
    pygame.draw.rect(screen, 'white', (player1x, player1y, 25, 150))
    pygame.draw.rect(screen, 'white', (player2x, player2y, 25, 150))


    #This will show the changes done on the screen.
    pygame.display.flip()
    #This will make the frame rate stable at 60
    dt = clock.tick(60) / 1000

