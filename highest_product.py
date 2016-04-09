# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

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

from math import ceil
import ipdb

def highest_product_n(list_of_ints, k):
	"""
	return the largest product of k ints in the given list
	"""
	if len(list_of_ints) < k:
		raise Exception('Not enough elements in list')

	smallest_neg = []
	largest = []

	for val in list_of_ints:
		if val < 0:
			if len(smallest_neg) < (k):
				smallest_neg.append(val)
			elif val < smallest_neg[-1]:
				smallest_neg[1] = val
			smallest_neg = sorted(smallest_neg)

		if len(largest) < k:
			largest.append(val)
		elif val > largest[0]:
			largest[0] = val
		largest = sorted(largest)

	if largest[-1] < 0:
		return list_multiply(largest)

	product = 1
	cnt = 0

	for i in range(int(ceil(k/2.0))):
		if k - cnt == 1:
			product *= largest[-1]
			cnt+=1
			break
		
		elif len(smallest_neg) >= 2:
			negs_prod = list_multiply(smallest_neg[:2])
			large_prod = list_multiply(largest[-3:-1])
			if negs_prod > large_prod:
				product *= negs_prod
				smallest_neg = smallest_neg[2:]
			else:
				product *= list_multiply(largest[-3:-1])
				largest = largest[:-3]+largest[-1:]				

		else:
			product *= list_multiply(largest[-3:-1])
			largest = largest[:-3] + largest[-1:]

		cnt += 2

	return product


def list_multiply(ints_to_mult):
	return reduce(lambda x, y: x*y, ints_to_mult)

assert highest_product_n([-2,-1,-3,-4,-5], 3) == -6, highest_product_n([-2,-1,-3,-4,-5], 3)
assert highest_product_n([-2,-2,1,1,5], 3) == 20, highest_product_n([-2,-2,1,1,5], 3)
assert highest_product_n([-2,-2,3,2,5], 3) == 30
assert highest_product_n([-2,-1,-3,0,5], 3) == 30
assert highest_product_n([-3,0,5,3], 3) == 0
assert highest_product_n([-10,-10,1,3,2], 3) == 300
assert highest_product_n([2, 2, 2,-3,-3,-3,-3], 4) == 81 
assert highest_product_n([2, 2, 2,-3,-3,3,-3], 4) == 36
assert highest_product_n([-1,-2,-4,-3,0,-3], 4) == 72
