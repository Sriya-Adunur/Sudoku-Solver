# Defines functions for input and output.
# CSC 101, Project 4
# Given code, Summer '22
# NOTE: Do not alter this file.


def read_grid(filename):
    """
    Read a sudoku grid from a file.

    :param filename: A 9x9 CSV's filename
    :return: A 9x9 list of lists of integers
    """
    grid = []

    with open(filename, "r") as grid_file:
        for row in grid_file:
            grid.append([int(cell) for cell in row.split(",")])

    return grid


def print_grid(grid):
    """
    Print a sudoku grid.

    :param grid: A 9x9 list of lists of integers
    """
    for i in range(9):
        print("%d %d %d | %d %d %d | %d %d %d" % tuple(grid[i]))
        if i == 2 or i == 5:
            print("------+-------+------")
