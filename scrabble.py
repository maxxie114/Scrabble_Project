"""----------------------------- actual code --------------------------------"""

# import the pygame module, so you can use it
import pygame as pyg
import os

#test comment

# define a main function
def main():

    # initialize the pygame module
    pyg.init()
    # create a surface on screen that has the size of 240 x 180
    screen = pyg.display.set_mode((800, 800))

    # load image (it is in same directory)
    F_tile = pyg.image.load(os.path.join('tiles/F.png'))
    scrabble_board = pyg.image.load(os.path.join('scrabble_board_800px.png'))

    # resize image
    # picture = pygame.image.load(filename)
    F_tile = pyg.transform.scale(F_tile, (40, 40))
    # blit image to screen
    screen.fill((255,255,255))
    screen.blit(scrabble_board, (0, 0))
    screen.blit(F_tile, (380, 364))

    # update the screen to make the changes visible (fullscreen update)
    pyg.display.flip()

    # define a variable to control the main loop
    running = True


    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pyg.event.get():
            # only do something if the event if of type QUIT
            if event.type == pyg.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
