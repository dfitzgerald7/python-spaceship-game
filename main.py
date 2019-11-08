import pygame
from pygame.locals import *
# define a main function

def getCartStep(x, y, angle):
    pass

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
    myVector = pygame.math.Vector2(-10,0)
    stepX = 0
    stepy = 0
    angle = 0

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        
        keys=pygame.key.get_pressed()
        
        if keys[K_LEFT]:
            pass
        elif keys[K_RIGHT]:
            pass
        elif keys[K_UP]:
            myVector[1] -= 1
        else:
            if myVector[1] < 0:
                myVector.update(myVector[0], m)
            if myVector[0] > 0:
                stepX -= .01
            if myVector < 0:
                stepX += .01
        # event handling, gets all event from the event queue

        #draw ship
        screen.fill((0,0,0))
        screen.blit(rotatedSpaceship, (myVector))
        
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