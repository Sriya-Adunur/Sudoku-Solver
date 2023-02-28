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
    pass


def check_col(grid, col):
    """
    Check the validity of a column in a sudoku grid.
    TODO: Complete this function.

    :param grid: A 9x9 list of lists of integers
    :param col: A column index within the grid
    :return: Whether or not the column has either 0 or 1 of each of the
             integers {1, ..., 9}
    """
    pass


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
    pass


def fill_grid(grid):
    """
    Fill a solvable sudoku grid.
    TODO: Complete this function.

    :param grid: A 9x9 list of lists of integers
    :return: The grid, such that each row, column, and 3x3 subgrid has exactly
             1 of each of the integers {1, ..., 9}
    """
    pass
