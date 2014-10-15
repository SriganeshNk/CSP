# SUDOKU CHECKER

from sudokuUtil import *

def check_solution(puzzle, solution):
    """Check the suggested solution."""
    # type check
    if not isinstance(solution, list):
        print "Error: solution is not a 2-D list."
        print "not a solution."
        return
    if len(solution) != 9:
        print "Error: wrong column size."
        print "not a solution."
        return
    for row in solution:
        if not isinstance(row, list):
            print "Error: solution is not a 2-D list."
            print "not a solution."
            return
        if len(row) != 9:
            print "Error: wrong row size."
            print "not a solution."
            return

    # equality check
    for i in range(9):
        for j in range(9):
            n = solution[i][j]
            if (not isinstance(n, int)) or (n < 1) or (n > 9):
                print "Error: strange number", n, "in row", i, "column", j
                print "not a solution."
                return
            if puzzle[i][j] != 0 and puzzle[i][j] != n:
                print "Error: number in place", i, j, "changed."
                print "not a solution."
                return

    # block correctness check
    for x in range(3):
        for y in range(3):
            bit_map = [0] * 9
            for i in range(3):
                for j in range(3):
                    n = solution[3*x+i][3*y+j]
                    bit_map[n - 1] = 1
            if sum(bit_map) != 9:
                print "Error: block", x, y, "error"
                print "not a solution."
                return

    # row correctness check
    for i in range(9):
        bit_map = [0] * 9
        for j in range(9):
            n = solution[i][j]
            bit_map[n - 1] = 1
        if sum(bit_map) != 9:
            print "Error: row", i, "error"
            print "not a solution."
            return

    # column correctness check
    transpose_solution = map(list, zip(*solution))
    for i in range(9):
        bit_map = [0] * 9
        for j in range(9):
            n = transpose_solution[i][j]
            bit_map[n - 1] = 1
        if sum(bit_map) != 9:
            print "Error: column", i, "error"
            print "not a solution."
            return

    print "solution checked."

#===================================================#
puzzle = load_sudoku("puzzle.txt")
solution = load_sudoku("solution.txt")
display(solution)
check_solution(puzzle, solution)

