# import the pygame module, so you can use it
import pygame as pyg
import os
default = 1            
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
            "Z":'tiles/Z.png',
}
# create class
class Tile:
    tileScore ={"A":default, 
            "B":3 ,
            "C":3 ,
            "D":default ,
            "E":default ,
            "F":4 ,
            "G":2 ,
            "H":4 , 
            "I":default , 
            "J":8 ,
            "K":5 ,
            "L":default , 
            "M":3 , 
            "N":default ,
            "O":default ,
            "P":3 ,
            "Q":10 , 
            "R":default ,
            "S":default ,
            "T":default ,
            "U":default ,
            "V":4 ,
            "W":4 ,
            "X":8 ,
            "Y":4 ,
            "Z":10 }


    # tile = pyg.image.load(os.path.join('tiles/F.png'))
    # declear variables
    # F_tile = pyg.image.load(os.path.join('tiles/F.png'))

    def __init__(self):
        pass
        # self.tileName = tileName
        # self.x = x
        # self.y = y
        # self.tile = tile\

    def loadImage(self,tileName):
        # if tileName == "F":
        tile = pyg.image.load(os.path.join(tileList[tileName]))
        # elif tileName == "G":
            # tile = pyg.image.load(os.path.join('tiles/G.png'))
        return tile

    def setSize(self,x,y,tile):
        newTile = pyg.transform.scale(tile, (x, y))
        return newTile
        # self.F_tile = F_tile 
        

    # def lordImage()
