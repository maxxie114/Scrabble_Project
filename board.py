# import the pygame module, so you can use it
import pygame as pyg
import os


# create class
class board:
    board = pyg.image.load(os.path.join('scrabble_board_800px.png'))

    def __init__(self):
        pass