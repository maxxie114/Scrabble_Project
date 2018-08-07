import pygame as pyg
import os
import random
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
# Create all the tile instances, there is a total of 95 instances
A_tile1 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile2 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile3 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile4 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile5 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile6 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile7 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile8 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile9 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
B_tile1 = Tile('B', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['B'])), (30, 30)), 'None')
B_tile2 = Tile('B', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['B'])), (30, 30)), 'None')
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
F_tile1 = Tile('F', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['F'])), (30, 30)), 'None')
F_tile2 = Tile('F', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['F'])), (30, 30)), 'None')
G_tile1 = Tile('G', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
G_tile2 = Tile('G', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
G_tile3 = Tile('G', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
H_tile1 = Tile('H', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['H'])), (30, 30)), 'None')
H_tile2 = Tile('H', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['H'])), (30, 30)), 'None')
I_tile1 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile2 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile3 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile4 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile5 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile6 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile7 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile8 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile9 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
J_tile1 = Tile('J', 8, pyg.transform.scale(pyg.image.load(os.path.join(tileList['J'])), (30, 30)), 'None')
K_tile1 = Tile('K', 5, pyg.transform.scale(pyg.image.load(os.path.join(tileList['K'])), (30, 30)), 'None')
L_tile1 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile2 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile3 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile4 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
M_tile1 = Tile('M', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['M'])), (30, 30)), 'None')
M_tile2 = Tile('M', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['M'])), (30, 30)), 'None')
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
P_tile1 = Tile('P', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['P'])), (30, 30)), 'None')
P_tile2 = Tile('P', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['P'])), (30, 30)), 'None')
Q_tile1 = Tile('Q', 10, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Q'])), (30, 30)), 'None')
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
V_tile1 = Tile('V', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['V'])), (30, 30)), 'None')
W_tile1 = Tile('W', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['W'])), (30, 30)), 'None')
X_tile1 = Tile('X', 8, pyg.transform.scale(pyg.image.load(os.path.join(tileList['X'])), (30, 30)), 'None')
Y_tile1 = Tile('Y', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Y'])), (30, 30)), 'None')
Y_tile2 = Tile('Y', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Y'])), (30, 30)), 'None')
Z_tile1 = Tile('Z', 10, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Z'])), (30, 30)), 'None')

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
# Use random to randomly select tiles
tileBank = random.sample(allTiles, len(allTiles))

def selectTile(player, number_of_tiles):
    """uses numpy to randomly select tiles and return a tileBack numpy array"""
    global tileBank
    player.tiles = np.append(player.tiles, tileBank[0:number_of_tiles])
    tileBank = tileBank[number_of_tiles:]
    return tileBank

# Create class Main
class Main:

    # Create a 15 * 15 grid
    board_list =   [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,A_tile1.image,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,A_tile1.image,0,0],
                    [0,0,0,0,0,0,A_tile1.image,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,A_tile1.image,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,A_tile1.image,0,0,0,0,0,0,0,0]]

    def __init__(self, screen):
        self.screen = screen
    
    def main():
        pyg.init()

    # Create all necessary colors
    blue_color = (0, 0, 255)
    green_color = (0, 255, 0)
    red_color = (255, 0, 0)
    #Display screen
    screen = pyg.display.set_mode((800, 700))
    screen.fill((255,255,255))
    scrabble_board = pyg.transform.scale(pyg.image.load(os.path.join('scrabble_board_800px.png')), (600, 600))
    screen.blit(scrabble_board, (0, 0))

    # Draw the grid
    for i in range(15):
        for j in range(15):
            # tiles_On_Board = pyg.transform.scale(pyg.image.load(os.path.join(tileList['F']))
            # screen.blit(A_tile1.image, (40 + j*35, 43 + i*35))
            if board_list[i][j] != 0:
                screen.blit(board_list[i][j], (40 + j*35, 41 + i*35))
    
    # screen.blit(A_tile1.image, (528, 537))



    # Coordinates
    # Middle: (285, 285)
    # Columns A-O: (43, 77, 112, 147, 181, 216, 250, 285, 319, 354, 388, 424, 458, 493, 528)
    # Rows 1-15: (33, 69, 105, 141, 177, 213, 249, 285, 321, 357, 393, 429, 465, 501, 538

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
# Run the Main method for pygame
if __name__=="__main__":
    Main.main()