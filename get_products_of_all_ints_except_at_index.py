'''
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.
'''
def get_products_of_all_ints_except_at_index(int_list):
	return_list = []
	for i in range(len(int_list)):
		return_list.append(reduce(lambda x,y: x*y, int_list[0:i]+int_list[i+1:]))

	return return_list

assert get_products_of_all_ints_except_at_index([1, 7, 3, 4]) == [84, 12, 28, 21]