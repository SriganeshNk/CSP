# UTILS

def load_sudoku(file_name):
    with open(file_name, "r") as f:
        data = f.read().splitlines()
    sudoku = []
    for row in data:
        sudoku_row_string = row.split()
        sudoku_row_int = [int(n) for n in sudoku_row_string]
        sudoku.append(sudoku_row_int)
    print "sudoku loaded from", file_name
    return sudoku

def save_sudoku(file_name, sudoku):
    with open(file_name, "w") as f:
        f.writelines(" ".join(str(j) for j in i) + "\n" for i in sudoku)
    print "sudoku saved to", file_name

def display(puzzle):
    for row in puzzle:
        print " ".join(str(n or "_") for n in row)

