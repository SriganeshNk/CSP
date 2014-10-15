# SUDOKU (NUMBER PLACE) PUZZLE FRAMEWORK
# Created by Arel Cordero November 12, 2005
# Modified by Le Hou September 17, 2014

import sys
from random import choice
from copy import deepcopy
from sudokuUtil import *

def construct_puzzle_solution():
    """Randomly arrange numbers in a grid while making all rows, columns and
    squares (sub-grids) contain the numbers 1 through 9. """
    # Loop until we're able to fill all 81 cells with numbers, while
    # satisfying the constraints above.
    while True:
        try:
            puzzle  = [[0]*9 for i in range(9)] # start with blank puzzle
            rows    = [set(range(1,10)) for i in range(9)] # set of available
            columns = [set(range(1,10)) for i in range(9)] #   numbers for each
            squares = [set(range(1,10)) for i in range(9)] #   row, column and square
            for i in range(9):
                for j in range(9):
                    # pick a number for cell (i,j) from the set of remaining available numbers
                    choices = rows[i].intersection(columns[j]).intersection(squares[(i/3)*3 + j/3])
                    random_choice = choice(list(choices))

                    puzzle[i][j] = random_choice

                    rows[i].discard(random_choice)
                    columns[j].discard(random_choice)
                    squares[(i/3)*3 + j/3].discard(random_choice)

            # success! every cell is filled.
            return puzzle

        except IndexError:
            # if there is an IndexError, we have worked ourselves in a corner (we just start over)
            pass

def pluck(puzzle, n = 20):
    """Randomly pluck out cells (numbers) from the solved puzzle grid."""
    cellsleft = set(range(81))
    while len(cellsleft) > n:
        cell = choice(list(cellsleft)) # choose a cell from ones we haven't tried
        cellsleft.discard(cell) # record that we are trying this cell
        puzzle[cell/9][cell%9] = 0 # 0 denotes a blank cell

def generate_puzzle(n):
    """Generate a puzzle based on a puzzle solution."""
    solution = construct_puzzle_solution()
    puzzle = deepcopy(solution)
    pluck(puzzle, n)
    return (puzzle, solution)

#===================================================#
puzzle_n = 30
if len(sys.argv) >= 2:
    puzzle_n = int(sys.argv[1])
print puzzle_n, 'existing numbers.'
(puzzle, given_solution) = generate_puzzle(puzzle_n)
display(puzzle)
save_sudoku('puzzle.txt', puzzle)
save_sudoku('given_solution.txt', given_solution)

