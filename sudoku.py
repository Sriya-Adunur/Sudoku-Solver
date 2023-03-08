# Brute forces sudoku puzzles.
# CSC 101, Project 4
# Given code, Summer '22
# TODO: Complete this file.

import sys
import sudoku_grids
import sudoku_io

def main():
    filename = sys.argv[1]
    grid = sudoku_io.read_grid(filename)
    filled = sudoku_grids.fill_grid(grid)
    sudoku_io.print_grid(filled)

if __name__ == "__main__":
    main()
