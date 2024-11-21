import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        #add if statements to take in user input.
        #hint look at event types and event keys.
    screen.fill("black")

    #add a circle to the screen. (look at pygame.draw.circle on the documentation)

    pygame.display.flip()

