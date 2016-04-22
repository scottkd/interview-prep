import numpy as np

def check_sudoku(puzzle_board):
	"""
	return true if the puzzle_board is a valid sudoku solution, else false.

	puzzle_board - 9x9 list of list of ints
	"""
	valids = set(range(1,10))

	puzzle_array = np.array(puzzle_board)

	# check each row
	for row in puzzle_array:
		if valids != set(row):
			return False

	# check each column by looking at transpose
	for col in puzzle_array.T:
		if valids != set(col):
			return False

	# check each sub-box
	for i in range(3):
		for j in range(3):
			box = set(puzzle_array[i*3:i*3+3, j*3:j*3+3])
			if valids != box:
				return False

	return True