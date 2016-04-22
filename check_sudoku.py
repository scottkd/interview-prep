import numpy as np

def check_sudoku(puzzle_board):
	valids = set(range(1,10))

	puzzle_array = np.array(puzzle_board)

	for row in puzzle_array:
		if valids != set(row):
			return False

	for col in puzzle_array.T:
		if valids != set(col):
			return False

	for i in range(3):

		for j in range(3):

			box = set(puzzle_array[i*3:i*3+3, j*3:j*3+3])

			if valids != box:
				return False

	return True