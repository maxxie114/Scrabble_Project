import os
import random
import numpy as np
from datascience import * 

class Tile:


    def __init__(self, name, score, image, modifier):
        self.name = name
        self.score = score
        self.image = image
        self.modifier = modifier

tileList = {"A":'tiles/A.png',
            "B":'tiles/B.png',
            "C":'tiles/C.png',
            "D":'tiles/D.png',
            "E":'tiles/E.png',
            "F":'tiles/F.png',
            "G":'tiles/G.png',
            "H":'tiles/H.png',
            "I":'tiles/I.png',
            "J":'tiles/J.png',
            "K":'tiles/K.png',
            "L":'tiles/L.png',
            "M":'tiles/M.png',
            "N":'tiles/N.png',
            "O":'tiles/O.png',
            "P":'tiles/P.png',
            "Q":'tiles/Q.png',
            "R":'tiles/R.png',
            "S":'tiles/S.png',
            "T":'tiles/T.png',
            "U":'tiles/U.png',
            "V":'tiles/V.png',
            "W":'tiles/W.png',
            "X":'tiles/X.png',
            "Y":'tiles/Y.png',
            "Z":'tiles/Z.png'}

A_tile1 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile2 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile3 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
B_tile = Tile('B', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['B'])), (30, 30)), 'None')
C_tile = Tile('C', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['C'])), (30, 30)), 'None')


allTiles = [A_tile1, A_tile2, A_tile3, B_tile, C_tile]
tilesTable = Table().with_column('Tiles', allTiles)
tileBank = tilesTable.sample(with_replacement = False).column(0)

def selectTile(player, number_of_tiles):
    player.tiles = np.append(player.tiles, tileBank[0:number_of_tiles])
    tileBank = tileBank[number_of_tiles:]
