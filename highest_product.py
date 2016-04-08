# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

def highest_product(list_of_ints):
	if len(list_of_ints) < 3:
		return 
	elif len(list_of_ints) == 3:
		return list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

	sorted_list = sorted(list_of_ints)
	largest_val = sorted_list[-1]
	negatives = []

	for val in sorted_list:
		if val < 0:
			negatives.append(val)

	if len(negatives) >= 2:
		if largest_val > 0 and (sorted_list[0] * sorted_list[1] > sorted_list[-2] * sorted_list[-3]):
			return largest_val * sorted_list[0] * sorted_list[1]
		
	return largest_val * sorted_list[-2] * sorted_list[-3]

assert highest_product([-2,-1,-3,-4,-5]) == -6
assert highest_product([-2,-2,1,1,5]) == 20
assert highest_product([-2,-2,3,2,5]) == 30
assert highest_product([-2,-1,-3,0,5]) == 30
assert highest_product([-3,0,5,3]) == 0


def highest_product_greedy(list_of_ints):
	if len(list_of_ints) < 3:
		return 
	elif len(list_of_ints) == 3:
		return list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

	neg_cnt = 0
	smallest_neg = []
	largest = []

	for val in list_of_ints:
		if val < 0:
			if len(smallest_neg) < 2:
				smallest_neg.append(val)
			elif val < smallest_neg[1]:
				smallest_neg[1] = val
			smallest_neg = sorted(smallest_neg)

		if len(largest) < 3:
			largest.append(val)
		elif val > largest[0]:
			largest[0] = val
		largest = sorted(largest)

	if largest[2]<=0:
		return largest[0] * largest[1] * largest[2]
	elif len(smallest_neg) == 2 and smallest_neg[0] * smallest_neg[1] > largest[0] * largest[1]:
		return smallest_neg[0]*smallest_neg[1]*largest[2]

	return largest[0] * largest[1] * largest[2]

assert highest_product_greedy([-2,-1,-3,-4,-5]) == -6
assert highest_product_greedy([-2,-2,1,1,5]) == 20
assert highest_product_greedy([-2,-2,3,2,5]) == 30
assert highest_product_greedy([-2,-1,-3,0,5]) == 30
assert highest_product_greedy([-3,0,5,3]) == 0
assert highest_product_greedy([-10,-10,1,3,2]) == 300


"""
cases:
	- all 3 negative
		- 3 largest values
	- 2 negative, 1 positive
		- 2 negatives product higher than 2 positives product
		- only 1 (or 2) positive
	- 1 negative, 2 positive
		- only 2 positive
		- check 0
	- all 3 positive
		- 3 largest values
"""