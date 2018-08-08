class Tile:

    def __init__(self,name):
        self.name = name

A_tile1 = Tile('A')

board_list =       [[0,0,0,0,A_tile1,A_tile1,A_tile1,0,0,0,0,0,0,0,0],
                    [0,0,A_tile1,A_tile1,A_tile1,0,0,0,0,0,0,0,0,0,0],
                    [A_tile1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [A_tile1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [A_tile1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [A_tile1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [A_tile1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [A_tile1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [A_tile1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [A_tile1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

# summation = []

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

a = getWords(15)
print(a)
# print(summation)
#words
