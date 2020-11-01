import random

#Function to print out the board
def displayBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#Takes the player input and puts 'X' and 'O' for their markers
def playerInput():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?\n').upper()

    if marker == 'X':
        return('X', 'O')
    else:
        return('O','X')

#Places marker on specified position on the board    
def placeMarker(board, marker, position):
    board[position] = marker

#Checks win condition by verifying if 3 specific positions have the same marker (not affected by )
def winCheck(board, mark):
    return((board[7] == mark and board[8] == mark and board[9] == mark) or #Across top
    (board[4] == mark and board[5] == mark and board[6] == mark) or #Across middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or #Across bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or #Down Left Side
    (board[8] == mark and board[5] == mark and board[2] == mark) or #Down middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or #Down Right Side
    (board[7] == mark and board[5] == mark and board[3] == mark) or #Diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) #Diagonal

def chooseFirst():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def spaceCheck(board, position):
    return board[position] == ' '

def fullBoardCheck(board):
    for i in range(1, 10):
        if spaceCheck(board, i):
            return False
    return True

def playerChoice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not spaceCheck(board, position):
        position = int(input('Choose your next position: (1-9)  '))
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1Marker, player2Marker = playerInput()
    turn = chooseFirst()
    print(turn + ' will go first!')

    gameOn = True

    while gameOn:
        if turn == 'Player 1':
            displayBoard(theBoard)
            position = playerChoice(theBoard)
            placeMarker(theBoard, player1Marker, position)

            if winCheck(theBoard, player1Marker):
                displayBoard(theBoard)
                print("Congratulations Player 1! You've won the game!")
                gameOn = False
            else:
                if fullBoardCheck(theBoard):
                    displayBoard(theBoard)
                    print('This game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        
        else:
            displayBoard(theBoard)
            position = playerChoice(theBoard)
            placeMarker(theBoard, player2Marker, position)

            if winCheck(theBoard, player2Marker):
                displayBoard(theBoard)
                print("Congratulations Player 2! You've won the game!")
                gameOn = False
            else:
                if fullBoardCheck(theBoard):
                    displayBoard(theBoard)
                    print('This game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    
    if not replay():
        break