# import the pygame module, so you can use it
import pygame as pyg
import os


# create class
class Tile:
    tile = pyg.image.load(os.path.join('tiles/F.png'))
    # declear variables
    # F_tile = pyg.image.load(os.path.join('tiles/F.png'))

    def __init__(self,x,y):
        # self.x = x
        # self.y = y
        pass
        # self.tile = tile

    # def setSize(self,x,y):
    #     return pyg.transform.scale(tile, (x, y))
    #     # self.F_tile = F_tile 
        

    # def lordImage()
