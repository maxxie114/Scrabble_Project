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
A_tile4 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile5 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile6 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile7 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile8 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile9 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')

B_tile1 = Tile('B', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['B'])), (30, 30)), 'None')
B_tile2 = Tile('B', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['B'])), (30, 30)), 'None')
C_tile1 = Tile('C', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['C'])), (30, 30)), 'None')
C_tile2 = Tile('C', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['C'])), (30, 30)), 'None')
D_tile1 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
D_tile2 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
D_tile3 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
D_tile4 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
E_tile1 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile2 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile3 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile4 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile5 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile6 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile7 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile8 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile9 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile10 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile11 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile12 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')

F_tile1 = Tile('F', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['F'])), (30, 30)), 'None')
F_tile2 = Tile('F', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['F'])), (30, 30)), 'None')
G_tile1 = Tile('G', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
G_tile2 = Tile('G', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
G_tile3 = Tile('G', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
H_tile1 = Tile('H', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['H'])), (30, 30)), 'None')
H_tile2 = Tile('H', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['H'])), (30, 30)), 'None')
I_tile1 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile2 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile3 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile4 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile5 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile6 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile7 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile8 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile9 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')

J_tile1 = Tile('J', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['J'])), (30, 30)), 'None')
K_tile1 = Tile('K', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['K'])), (30, 30)), 'None')
L_tile1 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile2 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile3 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile4 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
M_tile1 = Tile('M', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['M'])), (30, 30)), 'None')
M_tile2 = Tile('M', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['M'])), (30, 30)), 'None')
N_tile1 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile2 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile3 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile4 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile5 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile6 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
O_tile1 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile2 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile3 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile4 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile5 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile6 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile7 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile8 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')

P_tile1 = Tile('P', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['P'])), (30, 30)), 'None')
P_tile2 = Tile('P', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['P'])), (30, 30)), 'None')
Q_tile1 = Tile('Q', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Q'])), (30, 30)), 'None')
R_tile1 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile2 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile3 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile4 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile5 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile6 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
S_tile1 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
S_tile2 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
S_tile3 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
S_tile4 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
T_tile1 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile2 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile3 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile4 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile5 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile6 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
U_tile1 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')
U_tile2 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')
U_tile3 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')
U_tile4 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')

V_tile1 = Tile('V', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['V'])), (30, 30)), 'None')
W_tile1 = Tile('W', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['W'])), (30, 30)), 'None')
X_tile1 = Tile('X', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['X'])), (30, 30)), 'None')
Y_tile1 = Tile('Y', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Y'])), (30, 30)), 'None')
Y_tile2 = Tile('Y', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Y'])), (30, 30)), 'None')
Z_tile1 = Tile('Z', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Z'])), (30, 30)), 'None')


allTiles = [A_tile1, A_tile2, A_tile3, B_tile, C_tile]
tilesTable = Table().with_column('Tiles', allTiles)
tileBank = tilesTable.sample(with_replacement = False).column(0)

def selectTile(player, number_of_tiles):
    player.tiles = np.append(player.tiles, tileBank[0:number_of_tiles])
    tileBank = tileBank[number_of_tiles:]
