import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        #add if statements to take in user input. (make one for when a key is pressed and one when it is let go)

        #within the two if statements you should add nested if statements to determine which key was pressed
        #hint look at event types and event keys.
    screen.fill("black")

    #add a circle to the screen. (look at pygame.draw.circle on the documentation)

    pygame.display.flip()

