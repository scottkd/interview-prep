def make_change(amount, denominations):
	"""
	amount - total amount to change
	denominations - list of all denomination amounts

	return - list of all unique combinations of change
	"""
	if amount == 0:
		return 1
	elif amount < 0 or not denominations:
		return 0

	denom = denominations[0]
	denominations=denominations[1:]

	num_possibilities = 0
	while amount >= 0:
		num_possibilities += make_change(amount, denominations)
		amount -= denom

	return num_possibilities


assert make_change(4, [1]) == 1, make_change(4, [1])
assert make_change(3,[1,2,3,4]) == 3, make_change(3,[1,2,3,4])
assert make_change(4,[1,2,3,4]) == 5
