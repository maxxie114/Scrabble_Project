# import the pygame module, so you can use it
import pygame as pyg
import os
# import other classes
from tiles import *
from board import *
from display_panel import *



# create class
class Main:

	def __init__(self):
		pass
		# self.tile = tile
        # self.tiles = tiles

tile1 = Tile()
board1 = board()
def main():
	# initialize the pygame module
	# tile = Main()
	pyg.init()
	# create a surface on screen that has the size of 240 x 180
	screen = pyg.display.set_mode((800, 700))
	# Create an instant of display_panel
	panel1 = display_panel(screen)
	# load image (it is in same directory)
	F_tile = tile1.loadImage("Z")
	scrabble_board = board1.board
	# resize image
	# picture = pygame.image.load(filename)
	# F_tile = pyg.transform.scale(F_tile, (40, 40))
	F_tile = tile1.setSize(30,30,F_tile)
	scrabble_board = board1.setSize(600,600)
	# blit image to screen
	screen.fill((255,255,255))
	screen.blit(scrabble_board, (0, 0))
	screen.blit(F_tile, (527, 538))

	pyg.draw.rect(screen, panel1.blue_color, (0, 600, 600, 100), 5)
	pyg.draw.rect(screen, panel1.green_color, (600, 0, 200, 600), 5)

	panel1.drawTileBoxes(20)
	panel1.drawTileBoxes(20+60)
	panel1.drawTileBoxes(20+120)
	panel1.drawTileBoxes(20+180)
	panel1.drawTileBoxes(20+240)
	panel1.drawTileBoxes(20+300)
	panel1.drawTileBoxes(20+360)

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
	# define a main function


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
# call the main function
    main()
