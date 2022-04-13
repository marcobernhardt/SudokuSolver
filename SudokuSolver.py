from typing import Tuple

def print_board(board):
    '''
    Function that prints a 9x9 Sudoku board to the console in a nicely formatted way

    Parameters
    ----------
    board:  Matrix that represents a 9x9 Sudoku board
    '''

    print('\n')
    for i, row in enumerate(board):
        if i in [3, 6]:
            print("---------------------")
        for j, col in enumerate(row):
            if j in [3, 6]:
                print('| ', end="")
            print(col, end=' ') if j != 8 else print(col)


def is_valid(num: int, pos: Tuple[int, int], board):
    '''
    Function checks whether a possible insertion of number 1-9 is a valid solution.

    Parameters
    ----------

    num:    The number that is to be inserted
    pos:    Tuple of row index and column index where the number is to be inserted
    board:  Matrix that represents a 9x9 Sudoku board
    '''

    # check whether field is empty
    if board[pos[0]][pos[1]] != 0:
        return False

     # check row
    if num in board[pos[0]]:
        return False

    # check column
    for row in board:
        if num == row[pos[1]]:
            return False
        
    '''
    Check 3x3 square if number to be inserted is valid. The corresponding starting indices 
    of a square are determined by integer division and subsequent multiplication by 3.
    '''
    row_idx = pos[0]//3*3      # starting row-index    for searching the correpsonding 3x3 subgrid
    col_idx = pos[1]//3*3      # starting column-index for searching the correpsonding 3x3 subgrid

    # Loop over 3x3 subgrid using the starting row- and column index of the subgrid
    for i in range(3):
        for j in range(3):
            if board[row_idx+i][col_idx+j] == num:
                return False

    # If none of the checks return False, the insertion is valid
    return True

def get_free_pos(board) -> Tuple[int, int]:
    '''
    Function that returns the next free field in a 9x9 Sudoku board. The board is scanned in a row-first fashion.

    Parameters
    ----------
    board:  Matrix that represents a 9x9 Sudoku board
    '''
    
    # go through board row by row, column by column to find an empty field (=0)
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if col == 0:
                return (row_idx, col_idx)

def solve(b):
    '''
    Recursive function to solve a Sudoku board based on the backtracking algorithm.

    Parameters
    ----------
    board:  Matrix that represents a 9x9 Sudoku board
    '''

    free_pos = get_free_pos(b)      # get tuple of row- and column index of vacant field

    # base case: If there are no free spots, the board is solved  
    if not free_pos:
        return True


    # try numbers 1-9 in free spot 
    for i in range(1, 10):

        # If the number is a valid solution, insert into board
        if(is_valid(i, free_pos, b)):
            b[free_pos[0]][free_pos[1]] = i
            solve(b)

            # Check whether base case was reached 
            if solve(b):
                return True
            
        # Reset current position to zero
        b[free_pos[0]][free_pos[1]] = 0
    
    # Return False if none of the numbers 1-9 fit
    return False

# Sudoku board represented as a matrix
board = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
]


if __name__ == "__main__":
    solve(board)
    print_board(board)