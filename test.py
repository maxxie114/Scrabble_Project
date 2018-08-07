board_list =       [[0,0,0,0,'e','r','t',0,0,0,0,0,0,0,0],
                    [0,0,'p','o','o',0,0,0,0,0,0,0,0,0,0],
                    ['x',0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    ['r',0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    ['a',0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    ['b',0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    ['c',0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    ['w',0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    ['d',0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    ['e',0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

# summation = []

def checkColumn(column):
    """Scan all words that is bigger than length 1 and return a list 
        contains all those words"""
    words = []
    one_word = ''
    for i in range(15):
        if board_list[i][column] != 0:
            one_word += board_list[i][column]
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
            one_word += board_list[row][i]
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

getWords(15)

# print(summation)
#words
