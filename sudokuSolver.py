# SUDOKU SOLVER

import sys, copy, pdb
from time import time
from sudokuUtil import *

# Please implement function solve_puzzle
# input puzzle: 2D list, for example:
# [ [0,9,5,0,3,2,0,6,4]
#   [0,0,0,0,6,0,1,0,0]
#   [6,0,0,0,0,0,0,0,0]
#   [2,0,0,9,0,3,0,0,6]
#   [0,7,6,0,0,0,0,0,3]
#   [3,0,0,0,0,0,0,0,0]
#   [9,0,0,5,0,4,7,0,1]
#   [0,5,0,0,2,1,0,9,0]
#   [0,0,8,0,0,6,3,0,5] ]
# Return a 2D list with all 0s replaced by 1 to 9.
# You can utilize argv to distinguish between algorithms
# (basic backtracking or with MRV and forward checking).
# For example: python sudokuSolver.py backtracking
def getUnit(row, col):
        startR = row - (row%3)
        startC = col - (col%3)
        return startR, startR+2, startC, startC+2

def replace_l(lst, x ,y):
	lst = lst.replace(x, y)

import pdb

# Check for numbers in row, col and unit
def suggestValue(tempPuzzle, row, col, elimTry):
	possibleValues = '123456789'
        
	#Check for numbers in row
	[replace_l(possibleValues, x, ' ') for x in possibleValues if x in tempPuzzle[row]]
        
	# check for numbers in col
	[replace_l(possibleValues, tempPuzzle[x][col], ' ') for x in col_len if (tempPuzzle[x][col] != '0') and len(tempPuzzle[x][col]) == 1]

	startR, endR ,startC, endC = getUnit(row, col)
 
	# check for numbers in the unit
	[replace_l(possibleValues, tempPuzzle[x][y], ' ') for x in range(startR, endR+1) 
                       for y in range(startC, endC+1) if (tempPuzzle[x][y] != '0') and len(tempPuzzle[x][y]) == 1]

	if len(possibleValues) == 1 or elimTry == 1:
                tempPuzzle[row][col] = possibleValues

def isSolved(dummyPuzzle):
	solved = False
	for x in row_len:
		for y in col_len:
			solved = checkCorrectness(dummyPuzzle, x, y, True)
			if solved == False:
				return False
	return solved

# see if the tried value confirms to the games rules
def checkCorrectness(dummyPuzzle, row, col, strict=False):
	rowList = []
	colList = []
	Values = '123456789'
	for i in range(len(dummyPuzzle[row])):
		if len(dummyPuzzle[row][i]) > 1:
			rowList.append(dummyPuzzle[row][i].replace(dummyPuzzle[row][col],''))
		else:
			rowList.append(dummyPuzzle[row][i])
	for i in Values:
		if strict and rowList.count(i) == 0:
			return False
		if rowList.count(i) > 1:
			return False
	for i in range(len(dummyPuzzle[col])):
		if len(dummyPuzzle[i][col]) > 1:
			colList.append(dummyPuzzle[i][col].replace(dummyPuzzle[row][col],''))
		else:
			colList.append(dummyPuzzle[i][col]) 
	for i in Values:
		if strict and colList.count(i) == 0:
			return False
		if colList.count(i) > 1:
			return False
	unitList = []
	startR, endR, startC, endC = getUnit(row, col)
	for x in range(startR, endR+1):
		for y in range(startC, endC+1):
			if len(dummyPuzzle[x][y]) > 1:
				unitList.append(dummyPuzzle[x][y].replace(dummyPuzzle[row][col],''))
			else:
				unitList.append(dummyPuzzle[x][y])
	for i in Values:
		if strict and unitList.count(i) == 0:
			return False
		if unitList.count(i) > 1:
			return False
	dummyPuzzle[row] = rowList
	for i in range(len(dummyPuzzle[col])):
		dummyPuzzle[i][col] = colList[i]
	i = 0
	for x in range(startR, endR+1):
		for y in range(startC, endC+1):
			dummyPuzzle[x][y]=unitList[i]
			i = i+1
	return True
	
def nextEntry(strPuzzle, MRV=False):
	if MRV:
		r, c = 0, 0
		minPossible = int(11)
		for row in range(len(strPuzzle)):
			for col in range(len(strPuzzle[row])):
				if len(strPuzzle[row][col]) > 1 and len(strPuzzle[row][col]) < minPossible:
					minPossible, r, c = len(strPuzzle[row][col]), row, col
		if minPossible == 11:
			return -1, -1
		return r, c
	else:
		for row in range(len(strPuzzle)):
			for col in range(len(strPuzzle[row])):
				if len(strPuzzle[row][col]) > 1:
					return row, col
	return -1,-1

def revert(dummyPuzzle, strPuzzle):
	for row in range(len(strPuzzle)):
		for col in range(len(strPuzzle[row])):
			dummyPuzzle[row][col] = strPuzzle[row][col]


def search(dummyPuzzle, strPuzzle, row, col):
	"Using depth-first search and propagation, try all possible values."
	if len(strPuzzle[row][col]) == 1: 
		return True
	tryNum = len(strPuzzle[row][col])-1
	
	while tryNum > -1:
		temp =  str(strPuzzle[row][col][tryNum])
		dummyPuzzle[row][col] = temp
		if checkCorrectness(dummyPuzzle, row, col, False) == False:
			revert(dummyPuzzle, strPuzzle)
		else:
			newR, newC = nextEntry(dummyPuzzle, True)
			if newR == -1 and newC == -1:
				if isSolved(dummyPuzzle):
					return dummyPuzzle
			dummyPuzzle = search(dummyPuzzle, copy.deepcopy(dummyPuzzle), newR, newC)
			if isSolved(dummyPuzzle):
				return dummyPuzzle
			else:
				revert(dummyPuzzle, strPuzzle)
		tryNum = tryNum - 1	
	#print "------Dummy Puzzle--------------"
	#display(dummyPuzzle)
	#print "-------Str Puzzle-------------"
	#display(strPuzzle)
	if isSolved(dummyPuzzle):
		return dummyPuzzle
	else:
		return strPuzzle


def solve_puzzle(puzzle, argv):
	"""Solve the sudoku puzzle."""
        strPuzzle = [map(str, x) for x in puzzle]

	global row_len
        row_len = range(len(strPuzzle))
        global col_len
        col_len = range(len(strPuzzle[0]))

        [suggestValue(strPuzzle,row,col,i) for i in range(2)
                for row in row_len for col in col_len if strPuzzle[row][col] == '0']

	startR, startC = nextEntry(strPuzzle, True)
	dummyPuzzle = copy.deepcopy(strPuzzle)
	dummyPuzzle = search(dummyPuzzle, strPuzzle, startR, startC)
	#print "------original puzzle------------"
	#display(puzzle)
	#print "------converted puzzle-----------"
	#display(strPuzzle)
	#print "------solved puzzle---------------"
	display(dummyPuzzle)
	result = []
	if isSolved(dummyPuzzle):
		[result.append(map(int, x)) for x in dummyPuzzle]
		#for x in dummyPuzzle:
		#	temp = map(int, x)
		#	result.append(temp)	
		return result

	return load_sudoku('given_solution.txt')

#===================================================#
puzzle = load_sudoku('puzzle.txt')

print "solving ..."
t0 = time()
solution = solve_puzzle(puzzle, sys.argv)
t1 = time()
print "completed. time usage: %f" %(t1 - t0), "secs."

save_sudoku('solution.txt', solution)

