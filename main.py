import pygame
from pygame.locals import *
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the log     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((500,500))
    
    # add spaceship
    spaceship = pygame.image.load("spaceship.jpg")
    spaceship = pygame.transform.scale(spaceship, (40,40))
    
    #spaceship coords 
    x = 250
    y = 250
    stepX = 0
    stepY = 0

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        
        keys=pygame.key.get_pressed()
        
        if keys[K_LEFT]:
            stepX = -1    
        elif keys[K_RIGHT]:
            stepX = 1
        elif keys[K_UP]:
            stepY = -1
        else:
            if stepY < 0:
                stepY += .01
            if stepX > 0:
                stepX -= .01
            if stepX < 0:
                stepX += .01
        # event handling, gets all event from the event queue
        screen.fill((0,0,0))
        screen.blit(spaceship, (x,y))
        x += stepX; y += stepY 
        pygame.display.flip()
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()