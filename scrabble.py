"""----------------------------- actual code --------------------------------"""

# import the pygame module, so you can use it
import pygame
import os

# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800, 800))

    # load image (it is in same directory)
    F_tile = pygame.image.load(os.path.join('f_tile.png'))
    scrabble_board = pygame.image.load(os.path.join('scrabble_board_800px.png'))

    # blit image to screen
    screen.fill((255,255,255))
    screen.blit(scrabble_board, (0, 0))
    screen.blit(F_tile, (380, 364))

    # update the screen to make the changes visible (fullscreen update)
    pygame.display.flip()


    # define a variable to control the main loop
    running = True


    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
