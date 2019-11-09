import pygame
from pygame.locals import *
import time
# define a main function

def rotateAndNormalize(vector, angleStep):
    rotated = vector.rotate(angleStep)
    return pygame.math.Vector2.normalize(rotated)



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
    myVector = pygame.math.Vector2(0,-1)
    newVector = pygame.math.Vector2(0,0)
    magnitude = .1
    angle = 0
    angleStep = 0

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # time.sleep(1)
        # angleStep = 0
        keys=pygame.key.get_pressed()
        
        if keys[K_LEFT] or keys[K_RIGHT]:
            if keys[K_LEFT]:
                angleStep += 10
            else: 
                angleStep -= 10
            newVector = rotateAndNormalize(myVector, -1 * angleStep)
            
        elif keys[K_UP]:
            myVector += newVector

        #movement is constant due to no friction
        x += magnitude * myVector[0]
        y += magnitude * myVector[1] 
        # event handling, gets all event from the event queue

        #rotate vector, normalize and get x and y coords to be used with magnitude



        #draw ship
        screen.fill((0,0,0))
        pygame.draw.line(screen, (0,0,225), (x,y), (x + 50*myVector[0], y + 50*myVector[1]))
        pygame.draw.line(screen, (0,225,0), (x,y), (x + 50*newVector[0],y + 50*newVector[1]))
        rotatedSpaceship = pygame.transform.rotate(spaceship, angle+angleStep)
        screen.blit(rotatedSpaceship, (x, y))
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