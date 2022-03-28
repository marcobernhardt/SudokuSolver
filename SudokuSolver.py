# function that takes the sudoku board as input and prints it neatly onto the terminal
def print_board(board):
    print('\n')
    for i, row in enumerate(board):
        if i in [3, 6]:
            print("---------------------")
        for j, col in enumerate(row):
            if j in [3, 6]:
                print('| ', end="")
            print(col, end=' ') if j != 8 else print(col)


board = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,4,0,0,1,2,0],
            [0,7,0,4,0,0,1,2,0],
            [1,2,0,4,0,0,1,2,0],
            [0,4,9,4,0,0,1,2,0]
]


if __name__ == "__main__":
    print_board(board)
    # do stuff