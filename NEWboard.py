import pygame as pyg
import os

class Main:

	def __init__(self, screen):
		self.screen = screen

	def main():
		pyg.init()

	#Display screen
	screen = pyg.display.set_mode((800, 700))
	screen.fill((255,255,255))
	scrabble_board = pyg.transform.scale(pyg.image.load(os.path.join('scrabble_board_800px.png')), (600, 600))
	screen.blit(scrabble_board, (0, 0))

	# Coordinates
	# Middle: (285, 285)
	# Columns A-O: (43, 77, 112, 147, 181, 216, 250, 285, 319, 354, 388, 424, 458, 493, 528)
	# Rows 1-15: (33, 69, 105, 141, 177, 213, 249, 285, 321, 357, 393, 429, 465, 501, 538


	blue_color = (0, 0, 255)
	green_color = (0, 255, 0)
	red_color = (255, 0, 0)

	pyg.draw.rect(screen, blue_color, (0, 600, 600, 100), 5)
	pyg.draw.rect(screen, green_color, (600, 0, 200, 600), 5)
	for i in range(7):
		pyg.draw.rect(screen, red_color, (20 + 60 * i, 625, 50, 50), 2)

	# update the screen to make the changes visible (fullscreen update)
	pyg.display.flip()
	# define a variable to control the main loop
	running = True

	while running:
		for event in pyg.event.get():
			if event.type == pyg.QUIT:
				running = False

if __name__=="__main__":
    main()
