# import the pygame module, so you can use it
import pygame as pyg
import os
# from Main import *

# create class
class display_panel:
    blue_color = (0, 0, 255)
    green_color = (0, 255, 0)
    red_color = (255, 0, 0)
    def __init__(self,screen):
        self.screen = screen
        # pass

    def drawTileBoxes(self,x_coord):
        return pyg.draw.rect(self.screen, display_panel.red_color, (x_coord, 610, 50, 80), 2)
    
