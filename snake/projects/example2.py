import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        #add if statements to take in user input.
        #hint look at event types and event keys.
    screen.fill("black")

    pygame.display.flip()

