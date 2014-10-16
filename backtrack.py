import sys, copy, pdb
from time import time
from sudokuUtil import *


def check_box(puzzle_row, puzzle_col, row, col, num):
	#print "row =",row,"col =",col,"num =",num
	a = [1 for x in range(3) for y in range(3) if puzzle_row[x+row][y+col] == num]
	#print a
	if 1 in a:
		return 1
	return 0

def check_validity(puzzle_row, puzzle_col, row, col, num):
	# Check num if present in that row
	ret_row = (1 if num in puzzle_row[row] else 0)

	# check num if present in that col
	ret_col = (1 if num in puzzle_col[col] else 0)

	ret_box = check_box(puzzle_row, puzzle_col, row-row%3, col-col%3, num)

	return ret_row | ret_col | ret_box

import pdb
			
def solve_puzzle(puzzle_row, puzzle_col):
	# Find a spot with 0,0
	spot = next(((i,j) for i,x in enumerate(puzzle_row) for j,y in enumerate(x) if y == 0), -1)
	if spot == -1:
		return 1

	(x,y) = spot # Has the x and y co-ordinate for 0 in the puzzle array
	#print "x,y",(x,y)
	#pdb.set_trace()

	for i in range(1,10):
		if not check_validity(puzzle_row, puzzle_col, x, y, i):
			puzzle_row[x][y] = i
			puzzle_col[y][x] = i
			if solve_puzzle(puzzle_row, puzzle_col):
				return 1
			puzzle_row[x][y] = 0
			puzzle_col[y][x] = 0
			#print "valid num =",i

	return 0

def solve():
	puzzle_row = load_sudoku('puzzle.txt')
	puzzle_col = [[]]

	global row_len
	row_len = range(len(puzzle_row))
	global col_len
	col_len = range(len(puzzle_row[0]))

#		print puzzle_row
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
	t0 = time()
	r = solve_puzzle(puzzle_row, puzzle_col)
	t1 = time()
	print "completed. time usage: %f" %(t1 - t0), "secs."	
	if r == 0:
		return (puzzle_row, False)
	return (puzzle_row, True)
	#save_sudoku('solution.txt', puzzle_row)

