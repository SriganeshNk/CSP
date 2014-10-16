import sys, copy, pdb
from time import time
from sudokuUtil import *

def check_validity(puzzle_row, puzzle_col, row, col, num):
	# Check num if present in that row
	ret_row = (1 if num in puzzle_row[row] else 0)

	# check num if present in that col
	ret_col = (1 if num in puzzle_col[col] else 0)

	return ret_row | ret_col
			


def solve_puzzle(puzzle_row, puzzle_col, argv):
	# Find a spot with 0,0
	spot = next(((i,j) for i,x in enumerate(puzzle_row) for j,y in enumerate(x) if y == 0), -1)
	if spot == -1:
		return true

	(x,y) = spot # Has the x and y co-ordinate for 0 in the puzzle array
	print "x,y",(x,y)

	for i in range(1,10):
		if not check_validity(puzzle_row, puzzle_col, x, y, i):
			puzzle_row[x][y] = i
			print "valid num =",i

	return []

def solve():
	for i in range(2):
		puzzle_row = load_sudoku('puzzle.txt')
		puzzle_col = [[]]

		global row_len
		row_len = range(len(puzzle_row))
		global col_len
		col_len = range(len(puzzle_row[0]))

		print puzzle_row
		for x in row_len:
			lst=[]
			for i in col_len:
				lst.append(puzzle_row[i][x])
			puzzle_col.append(lst)

		del puzzle_col[0]

		# By this point we are having two list of vectors
		# Puzzle_row is a list of vectors where each vector is a row
		# Puzzle_col is a list of vectors where each vector is a col
		# Pass both these values to the sudoku solver
		solution = solve_puzzle(puzzle_row, puzzle_col,sys.argv)
		save_sudoku('solution.txt', solution)

solve()
