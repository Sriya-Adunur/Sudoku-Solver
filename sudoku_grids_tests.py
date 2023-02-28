# Tests functions for sudoku grids.
# CSC 101, Project 4
# Given tests, Summer '22

import unittest
import sudoku_grids


class TestSudokuGrids(unittest.TestCase):
    def test01_check_row(self):
        grid = [[3, 2, 0, 0, 0, 0, 0, 5, 0],
                [1, 0, 0, 6, 0, 0, 9, 3, 0],
                [9, 0, 0, 7, 1, 0, 8, 0, 0],
                [4, 7, 8, 9, 5, 0, 0, 2, 6],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [2, 6, 0, 0, 3, 7, 5, 4, 1],
                [0, 0, 2, 0, 7, 6, 0, 0, 3],
                [0, 4, 3, 0, 0, 2, 0, 0, 5],
                [0, 1, 0, 0, 0, 0, 0, 7, 9]]

        self.assertTrue(sudoku_grids.check_row(grid, 0))
        grid[0][2] = 1
        self.assertTrue(sudoku_grids.check_row(grid, 0))
        grid[0][3] = 1
        self.assertFalse(sudoku_grids.check_row(grid, 0))

    def test02_check_col(self):
        grid = [[3, 2, 0, 0, 0, 0, 0, 5, 0],
                [1, 0, 0, 6, 0, 0, 9, 3, 0],
                [9, 0, 0, 7, 1, 0, 8, 0, 0],
                [4, 7, 8, 9, 5, 0, 0, 2, 6],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [2, 6, 0, 0, 3, 7, 5, 4, 1],
                [0, 0, 2, 0, 7, 6, 0, 0, 3],
                [0, 4, 3, 0, 0, 2, 0, 0, 5],
                [0, 1, 0, 0, 0, 0, 0, 7, 9]]

        self.assertTrue(sudoku_grids.check_col(grid, 0))
        grid[4][0] = 5
        self.assertTrue(sudoku_grids.check_col(grid, 0))
        grid[6][0] = 1
        self.assertFalse(sudoku_grids.check_col(grid, 0))

    def test03_check_subgrid(self):
        grid = [[3, 2, 0, 0, 0, 0, 0, 5, 0],
                [1, 0, 0, 6, 0, 0, 9, 3, 0],
                [9, 0, 0, 7, 1, 0, 8, 0, 0],
                [4, 7, 8, 9, 5, 0, 0, 2, 6],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [2, 6, 0, 0, 3, 7, 5, 4, 1],
                [0, 0, 2, 0, 7, 6, 0, 0, 3],
                [0, 4, 3, 0, 0, 2, 0, 0, 5],
                [0, 1, 0, 0, 0, 0, 0, 7, 9]]

        self.assertTrue(sudoku_grids.check_subgrid(grid, 0, 0))
        grid[1][1] = 8
        self.assertTrue(sudoku_grids.check_subgrid(grid, 0, 0))
        grid[0][2] = 1
        self.assertFalse(sudoku_grids.check_subgrid(grid, 0, 0))

    def test04_fill_grid(self):
        grid = [[3, 2, 0, 0, 0, 0, 0, 5, 0],
                [1, 0, 0, 6, 0, 0, 9, 3, 0],
                [9, 0, 0, 7, 1, 0, 8, 0, 0],
                [4, 7, 8, 9, 5, 0, 0, 2, 6],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [2, 6, 0, 0, 3, 7, 5, 4, 1],
                [0, 0, 2, 0, 7, 6, 0, 0, 3],
                [0, 4, 3, 0, 0, 2, 0, 0, 5],
                [0, 1, 0, 0, 0, 0, 0, 7, 9]]

        soln = [[3, 2, 6, 4, 8, 9, 1, 5, 7],
                [1, 8, 7, 6, 2, 5, 9, 3, 4],
                [9, 5, 4, 7, 1, 3, 8, 6, 2],
                [4, 7, 8, 9, 5, 1, 3, 2, 6],
                [5, 3, 1, 2, 6, 4, 7, 9, 8],
                [2, 6, 9, 8, 3, 7, 5, 4, 1],
                [8, 9, 2, 5, 7, 6, 4, 1, 3],
                [7, 4, 3, 1, 9, 2, 6, 8, 5],
                [6, 1, 5, 3, 4, 8, 2, 7, 9]]

        self.assertEqual(sudoku_grids.fill_grid(grid), soln)


if __name__ == "__main__":
    unittest.main()
