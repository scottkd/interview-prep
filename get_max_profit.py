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

# No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).


def get_max_profit(stock_prices_yesterday):
	local_min = stock_prices_yesterday[0], 0
	local_max = 0, 0
	max_diff_at_buy_price = []
	diff = []
	for i in range(len(stock_prices_yesterday)-1):
		buy_price = stock_prices_yesterday[i]
		diff.insert(i, [])
		for j in range(i+1,len(stock_prices_yesterday)):
			sell_price = stock_prices_yesterday[j]
			diff[i].append(sell_price - buy_price)
		max_diff_at_buy_price.append(max(diff[i]))
	return max(max_diff_at_buy_price)
