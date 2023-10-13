from random import randrange
from copy import copy

# declaring Computer and player symbols
player, computer = "X", "O"
print("player: X \ncomputer: O")

# generating the board
board = list(range(1, 10))
# all wins conditions
wins = ((0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6))


# printing board in a matrix style
def print_board():
    print()
    j = 0
    for i in board:
        j += 1
        print(f"[{i}]", end=" ")
        # new line after every 3 boxes
        if j % 3 == 0:
            print()


# if there is an empty box
def has_empty_space():
    return (board.count("X") + board.count("O")) < 9


# confirm moving (and testing movement)
def make_move(plyr, mve, undo=False):
    # if the player can do the movement
    if can_move(mve):
        # if it's not a test
        if not undo:
            board[mve - 1] = plyr
            win = is_winner(plyr, board)
            return True, win

        # when it's a test movement
        b = copy(board)
        b[mve - 1] = plyr
        # checking if with that move computer wins
        win = is_winner(plyr, b)
        return True, win

    return False, False


# if the entered number is correct to making a move
def can_move(mve):
    # return -> True, if: move in range(1,10) and is a int (not used for both players)
    return 1 <= mve <= 9 and isinstance(board[mve - 1], int)


# making a move for computer
def computer_move():
    # initialize mv for confirming the movement
    mv = -1
    # check all boxes
    for i in range(1, 10):
        # if computer can win -> do that move
        if make_move(computer, i, True)[1]:
            mv = i
            break

    # if still computer doesn't have a good movement
    if mv == -1:
        # check all boxes
        for i in range(1, 10):
            # if computer can stop the player from winning
            if make_move(player, i, True)[1]:
                mv = i
                break

    # if still computer doesn't have a good movement
    if mv == -1:
        while True:
            # computer make a random movement
            if make_move(computer, r := randrange(1, 10), True)[0]:
                mv = r
                break

    # confirming the last correct move for computer
    make_move(computer, mv)


# If the player or the computer wins
def is_winner(plyr, brd):
    for tup in wins:
        for w in tup:
            if brd[w] != plyr:
                break
        else:
            return True


# starting the game in a while loop until one of the players wins
while has_empty_space():
    print_board()
    move = int(input("Enter your selected box: "))
    mv, win = make_move(player, move)
    if not mv:
        print("movement not confirmed!! (Enter 1-9)")
        continue

    # if player wins the game
    if win:
        print_board()
        print('>> you won')
        exit()

    # Making a move for computer if there is and empty space
    if has_empty_space():
        computer_move()

    # if computer wins the game
    if is_winner(computer, board):
        print_board()
        print('>> you loose!!')
        exit()

# there is no empty space for any move and no winner
print_board()
print(">> Game over....")

