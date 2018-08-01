
# import the pygame module, so you can use it
import pygame as pyg
import os


# define a main function
def main():

    # initialize the pygame module
    pyg.init()
    # create a surface on screen
    screen = pyg.display.set_mode((800, 700))

    # load images in same directory
    F_tile = pyg.image.load(os.path.join('tiles/F.png'))
    scrabble_board = pyg.image.load(os.path.join('scrabble_board_800px.png'))

    # resize images
    F_tile = pyg.transform.scale(F_tile, (30, 30))
    scrabble_board = pyg.transform.scale(scrabble_board, (600, 600))

    # Coordinates
    # Middle: (285, 285)
    # Column A: (43)
    # Column O: (527)
    # Row 1: (33)
    # Row 15: (538)


    # blit images to screen
    screen.fill((255,255,255))
    screen.blit(scrabble_board, (0, 0))
    screen.blit(F_tile, (527, 538))

    blue_color = (0, 0, 255)
    green_color = (0, 255, 0)
    red_color = (255, 0, 0)

    pyg.draw.rect(screen, blue_color, (0, 600, 600, 100), 5)
    pyg.draw.rect(screen, green_color, (600, 0, 200, 600), 5)

    def drawTileBoxes(x_coord):
        return pyg.draw.rect(screen, red_color, (x_coord, 610, 50, 80), 2)

    drawTileBoxes(20)
    drawTileBoxes(20+60)
    drawTileBoxes(20+120)
    drawTileBoxes(20+180)
    drawTileBoxes(20+240)
    drawTileBoxes(20+300)
    drawTileBoxes(20+360)

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
