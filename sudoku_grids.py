# Defines functions for sudoku grids.
# CSC 101, Project 4
# Given code, Summer '22


def check_row(grid, row):
    """
    Check the validity of a row in a sudoku grid.
    TODO: Complete this function.

    :param grid: A 9x9 list of lists of integers
    :param row: A row index within the grid
    :return: Whether or not the row has either 0 or 1 of each of the
             integers {1, ..., 9}
    """
    r = []
    for element in grid[row]:
        if element != 0:
            if element not in r:            
                r.append(element)
            else:
                return False
    return True


def check_col(grid, col):
    """
    Check the validity of a column in a sudoku grid.
    TODO: Complete this function.

    :param grid: A 9x9 list of lists of integers
    :param col: A column index within the grid
    :return: Whether or not the column has either 0 or 1 of each of the
             integers {1, ..., 9}
    """
    r = []
    for i in range(len(grid)):
        if grid[i][col] != 0:
            if grid[i][col] not in r:
                r.append(grid[i][col])
            else:
                return False
    return True


def check_subgrid(grid, row, col):
    """
    Check the validity of a subgrid in a sudoku grid.
    TODO: Complete this function.

    :param grid: A 9x9 list of lists of integers
    :param row: A row index within the grid
    :paral col: A column index within the grid
    :return: Whether or not the 3x3 subgrid containing that row and column has
             either 0 or 1 of each of the integers {1, ..., 9}
    """
    r = []

    if row >= 0 and row < 3:
        row = 0
    elif row >= 3 and row < 6:
        row = 3
    else:
        row = 6

    if col >= 0 and col < 3:
        col = 0
    elif col >= 3 and col < 6:
        col = 3
    else:
        col = 6     

    for i in range(row, row+3):
        for j in range(col, col+3):
            if grid[i][j] != 0:
                if grid[i][j] not in r:
                    r.append(grid[i][j])
                else:
                    return False
    return True

def valid_grid(grid):
    for i in range(9):
        for j in range(9):
            if (grid[i][j] == 0) or not check_row(grid, i) or not check_col(grid, j) or not check_subgrid(grid, i, j):
                return False
    return True




def valid_num(grid, row, col):
    i = 1
    while i < 10:
        grid[row][col] = i
        if check_row(grid, row) and check_col(grid, col) and check_subgrid(grid, row, col):
            return True
        else:
            i = i + 1
    return False

def replace(grid, row, col):
    i = 1
    while i < 10:
        grid[row][col] = i
        if check_row(grid, row) and check_col(grid, col) and check_subgrid(grid, row, col):
            return i
        else:
            i = i + 1

def valid_b(grid, row, col):
    num = grid[row][col] 
    i = 1 
    while i < 10:
        grid[row][col] = i
        if check_row(grid, row) and check_col(grid, col) and check_subgrid(grid, row, col) and i != num:
            grid[row][col] = num
            return True
        else:
            i = i + 1
    return False

def replace_b(grid, row, col):
    num = grid[row][col]
    i = 1
    while i < 10:
        grid[row][col] = i
        if check_row(grid, row) and check_col(grid, col) and check_subgrid(grid, row, col) and i != num:
            return i
        else:
            i = i + 1
                     

def backtrack(grid, gcpy, row, col):
    gcpy[row][col] = 0
    if col == 0:
        j = 8
        i = row - 1
    else:
        j = col - 1
        i = row
    while i >= 0 and  j >= 0:
        if grid[i][j] != 0:
            if j == 0:
                j = 8
                i = i - 1
            else:
                j = j - 1
        elif valid_b(gcpy, i, j):
            gcpy[i][j] = replace_b(gcpy, i, j)
            return gcpy
        else:
            gcpy[i][j] = 0
            if j == 0:
                j = 8
                i = i - 1
            else:
                j = j - 1
    
    

def fill_grid(grid):
    """
    Fill a solvable sudoku grid.
    TODO: Complete this function.

    :param grid: A 9x9 list of lists of integers
    :return: The grid, such that each row, column, and 3x3 subgrid has exactly
             1 of each of the integers {1, ..., 9} 
  
    """ 
    gcpy = [row.copy() for row in grid] 
    row = 0
    col = 0
    while row < 9 and col < 9:
        if grid[row][col] != 0:
            col = col
        elif valid_num(gcpy, row, col):
            gcpy[row][col] = replace(gcpy, row, col)
        else:
            gcpy = backtrack(grid, gcpy, row, col)
        if col == 8:
            col = 0
            row = row + 1
        else:
            col = col + 1
    return gcpy
