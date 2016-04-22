# Writing programming interview questions hasn't made me rich. Maybe trading Apple stocks will.
# Suppose we could access yesterday's stock prices as a list, where:

# The indices are the time in minutes past trade opening time, which was 9:30am local time.
# The values are the price in dollars of Apple stock at that time.
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

# Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

# For example:

#   stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# get_max_profit(stock_prices_yesterday)
# # returns 6 (buying for $5 and selling for $11)

# No "shorting" - you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).

def get_max_profit(stock_prices_yesterday):
	# init max_diff and curr_min using first two values of list
	max_diff = stock_prices_yesterday[1] - stock_prices_yesterday[0]
	curr_min = min(stock_prices_yesterday[0], stock_prices_yesterday[1])

	# iterate over list, skipping first two elements that were handled
	for i in range(2, len(stock_prices_yesterday)):
		curr_item = stock_prices_yesterday[i]
		curr_diff = curr_item - curr_min
		
		# make any necessary changes to max_diff and curr_min
		max_diff = max(max_diff, curr_diff)
		curr_min = min(curr_min, curr_item)

	return max_diff

assert get_max_profit([10, 7, 5, 8, 11, 9]) == 6
assert get_max_profit([10, 9, 7, 6, 4]) == -1
assert get_max_profit([1, 5, 10, 6, 4]) == 9