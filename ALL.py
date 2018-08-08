import pygame as pyg
import os
import random

# Declare all variables
# Create a dictionary to store all the images files
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

blue_color = (0, 0, 255)
green_color = (0, 255, 0)
red_color = (255, 0, 0)
orange_color = (255, 128, 0)
black_color = (0, 0, 0)
white_color = (255, 255, 255)



# Create classes
# Create class Player
class Player:

    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.score = 0
# Create 2 to 4 player instances
Player1 = Player('Player 1')
Player2 = Player('Player 2')

# Create class Tile
class Tile:

    
    def __init__(self, name, score, image, modifier):
        self.name = name
        self.score = score
        self.image = image
        self.modifier = modifier


# Create all the Tile instances, there is a total of 95 instances
# A
A_tile1 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile2 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile3 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile4 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile5 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile6 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile7 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile8 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile9 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
# B
B_tile1 = Tile('B', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['B'])), (30, 30)), 'None')
B_tile2 = Tile('B', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['B'])), (30, 30)), 'None')
# C
C_tile1 = Tile('C', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['C'])), (30, 30)), 'None')
C_tile2 = Tile('C', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['C'])), (30, 30)), 'None')
# D
D_tile1 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
D_tile2 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
D_tile3 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
D_tile4 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
# E
E_tile1 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile2 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile3 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile4 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile5 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile6 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile7 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile8 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile9 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile10 = Tile('E',1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile11 = Tile('E',1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile12 = Tile('E',1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
# F
F_tile1 = Tile('F', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['F'])), (30, 30)), 'None')
F_tile2 = Tile('F', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['F'])), (30, 30)), 'None')
# G
G_tile1 = Tile('G', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
G_tile2 = Tile('G', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
G_tile3 = Tile('G', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
# H
H_tile1 = Tile('H', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['H'])), (30, 30)), 'None')
H_tile2 = Tile('H', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['H'])), (30, 30)), 'None')
# I
I_tile1 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile2 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile3 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile4 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile5 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile6 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile7 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile8 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile9 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
# J
J_tile1 = Tile('J', 8, pyg.transform.scale(pyg.image.load(os.path.join(tileList['J'])), (30, 30)), 'None')
# K
K_tile1 = Tile('K', 5, pyg.transform.scale(pyg.image.load(os.path.join(tileList['K'])), (30, 30)), 'None')
# L
L_tile1 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile2 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile3 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile4 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
# M
M_tile1 = Tile('M', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['M'])), (30, 30)), 'None')
M_tile2 = Tile('M', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['M'])), (30, 30)), 'None')
# N
N_tile1 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile2 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile3 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile4 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile5 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile6 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
# O
O_tile1 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile2 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile3 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile4 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile5 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile6 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile7 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile8 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
# P
P_tile1 = Tile('P', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['P'])), (30, 30)), 'None')
P_tile2 = Tile('P', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['P'])), (30, 30)), 'None')
# Q
Q_tile1 = Tile('Q',10, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Q'])), (30, 30)), 'None')
# R
R_tile1 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile2 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile3 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile4 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile5 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile6 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
# S
S_tile1 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
S_tile2 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
S_tile3 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
S_tile4 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
# T
T_tile1 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile2 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile3 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile4 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile5 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile6 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
# U
U_tile1 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')
U_tile2 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')
U_tile3 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')
U_tile4 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')
# V
V_tile1 = Tile('V', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['V'])), (30, 30)), 'None')
# W
W_tile1 = Tile('W', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['W'])), (30, 30)), 'None')
# X
X_tile1 = Tile('X', 8, pyg.transform.scale(pyg.image.load(os.path.join(tileList['X'])), (30, 30)), 'None')
# Y
Y_tile1 = Tile('Y', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Y'])), (30, 30)), 'None')
Y_tile2 = Tile('Y', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Y'])), (30, 30)), 'None')
# Z
Z_tile1 = Tile('Z',10, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Z'])), (30, 30)), 'None')

# Put them all into a list
allTiles = [A_tile1, A_tile2, A_tile3, A_tile4, A_tile5, A_tile6, A_tile7, A_tile8, A_tile9, 
            B_tile1, B_tile2, C_tile1, C_tile2, D_tile1, D_tile2, D_tile3, D_tile4, 
            E_tile1, E_tile2, E_tile3, E_tile4, E_tile5, E_tile6, E_tile7, E_tile8, E_tile9, E_tile10, E_tile11, E_tile12, 
            F_tile1, F_tile2, G_tile1, G_tile2, G_tile3, H_tile1, H_tile2, 
            I_tile1, I_tile2, I_tile3, I_tile4, I_tile5, I_tile6, I_tile7, I_tile8, I_tile9, 
            J_tile1, K_tile1, L_tile1, L_tile2, L_tile3, L_tile4, M_tile1, M_tile2, 
            N_tile1, N_tile2, N_tile3, N_tile4, N_tile5, N_tile6, 
            O_tile1, O_tile2, O_tile3, O_tile4, O_tile5, O_tile6, O_tile7, O_tile8, 
            P_tile1, P_tile2, Q_tile1, R_tile1, R_tile2, R_tile3, R_tile4, R_tile5, R_tile6, 
            S_tile1, S_tile2, S_tile3, S_tile4, T_tile1, T_tile2, T_tile3, T_tile4, T_tile5, T_tile6, 
            U_tile1, U_tile2, U_tile3, U_tile4, V_tile1, W_tile1, X_tile1, Y_tile1, Y_tile2, Z_tile1]

# Create a 15 * 15 grid
board_list =   [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,A_tile1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,A_tile1,0,0],
                [0,0,0,0,0,0,A_tile1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,A_tile1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,A_tile1,0,0,0,0,0,0,0,0]]

# Use random to randomly select tiles
tileBank = random.sample(allTiles, len(allTiles))

def selectTile(player):
    """Return a list of 7 tiles added together with a given player object"""
    player.tiles.append(tileBank.pop())
    return player.tiles

for i in range(7):
    selectTile(Player1)
    selectTile(Player2)

print('Player 1 tiles: ' + str(Player1.tiles[0].name) + ', ' + str(Player1.tiles[1].name) + ', ' + str(Player1.tiles[2].name) + ', ' + (Player1.tiles[3].name) + ', ' 
+ (Player1.tiles[4].name) + ', ' + (Player1.tiles[5].name) + ', ' + (Player1.tiles[6].name)) # Test code

print('Player 2 tiles: ' + str(Player2.tiles[0].name) + ', ' + str(Player2.tiles[1].name) + ', ' + str(Player2.tiles[2].name) + ', ' + (Player2.tiles[3].name) + ', '
 + (Player2.tiles[4].name) + ', ' + (Player2.tiles[5].name) + ', ' + (Player2.tiles[6].name)) # Test code

#class Main:

# def __init__(self, screen):
#     self.screen = screen

# Pygame main function
def main():
    pyg.init()

    # Display screen
    screen = pyg.display.set_mode((800, 700))
    screen.fill((255,255,255))
    scrabble_board = pyg.transform.scale(pyg.image.load(os.path.join('scrabble_board_800px.png')), (600, 600))
    screen.blit(scrabble_board, (0, 0))

    # Draw boxes
    pyg.draw.rect(screen, blue_color, (0, 600, 600, 100), 5)
    pyg.draw.rect(screen, green_color, (600, 0, 200, 600), 5)
    for i in range(7):
        pyg.draw.rect(screen, red_color, (20 + 60 * i, 625, 50, 50), 2)


    # Place tiles in squares

    def showTiles(player):
        for i in range(7):
            screen.blit(player.tiles[i].image, (30 + 60*i, 635))

    showTiles(Player1)

    # screen.blit(Player1.tiles[0].image, (43, 33))  # Test code
    # screen.blit(Player1.tiles[1].image, (43, 69))  # Test code
    # screen.blit(Player1.tiles[2].image, (43, 105)) # Test code

    # Calculate score
    scoreCollection = []
    for i in range(15):
        for j in range(15):
            if board_list[i][j] != 0:
                scoreCollection.append(board_list[i][j].score)
    Score = sum(scoreCollection)
    print('Score is: ' + str(Score))




    # Draw the grid
    for i in range(15):
        for j in range(15):
            # tiles_On_Board = pyg.transform.scale(pyg.image.load(os.path.join(tileList['F']))
            # screen.blit(A_tile1.image, (40 + j*35, 43 + i*35))
            if board_list[i][j] != 0:
                screen.blit(board_list[i][j].image, (40 + j * 35, 41 + i * 35))

    # Update the screen to make the changes visible
    pyg.display.flip()

    # print('Player 1 tiles: ' + str(Player1.tiles[0].name) + ', ' + str(Player1.tiles[1].name))  # Test code
    # print('Player 2 tiles: ' + str(Player2.tiles[0].name) + ', ' + str(Player2.tiles[1].name))  # Test code

    # print(Player1.tiles[:]) # Test code
    # print(Player2.tiles[:]) # Test code

    # Coordinates
	# Middle: (285, 285)
	# Columns A-O: (43, 77, 112, 147, 181, 216, 250, 285, 319, 354, 388, 424, 458, 493, 528)
	# Rows 1-15: (33, 69, 105, 141, 177, 213, 249, 285, 321, 357, 393, 429, 465, 501, 538)

	# define a variable to control the main loop
    running = True
    # Attention: These should be included in main()
    while running:
	    for event in pyg.event.get():
		    if event.type == pyg.QUIT:
			    running = False


# Create functions


# Create functions for all calculations
def checkColumn(column):
    """Scan all words that is bigger than length 1 and return a list 
        contains all those words"""
    words = []
    one_word = ''
    for i in range(15):
        if board_list[i][column] != 0:
            one_word += board_list[i][column].name
        else:
            words.append(one_word)
            one_word = ''
    words.append(one_word)
    words = [x for x in words if len(x) > 1]
    return words


def checkRow(row):
    """Scan all words in a row that is bigger than length 1 and return a list 
        contains all those words"""
    words = []
    one_word = ''
    for i in range(15):
        if board_list[row][i] != 0:
            one_word += board_list[row][i].name
        else:
            words.append(one_word)
            one_word = ''
    words.append(one_word)
    words = [x for x in words if len(x) > 1]

    return words

def getWords(boardSize):
    summation = []
    for i in range(boardSize):
        summation.extend(checkRow(i))
        summation.extend(checkColumn(i))
    summation = [x for x in summation if len(x) > 0]
    return summation

if __name__=="__main__":
    main()
