def solve_sudoku(board):
    # print(f"{find_empty_cell(board)}")
    if not find_empty_cell(board):
        return True
    
    row, col = find_empty_cell(board)

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0

        return False
    
def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid_move(board, row, col, num):
    # check num availability in row
    if num in board[row]:
        return False
    
    for i in range(9):
        if board[i][col] == num:
            return False
        
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    print(f"{subgrid_row} === {subgrid_col}")

    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if board[i][j] == num:
                return False
            
    return True
# No solution
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# solve puzzle
# puzzle = [
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 5, 3, 4, 8],
#   [1, 9, 8, 3, 4, 2, 5, 6, 7],
#   [8, 5, 9, 7, 6, 1, 4, 2, 3],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 6, 1, 5, 3, 7, 2, 8, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]

if solve_sudoku(puzzle):
    print("Sudoku puzzle solved:")
    for row in puzzle:
        print(row)
else:
    print("No solution exists for the given Sudoku puzzle.")
