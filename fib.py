'''
Write a function fib() that a takes an integer n and returns the nth fibonacci  number.
Let's say our fibonacci series is 0-indexed and starts with 0. So:

  fib(0) # => 0
fib(1) # => 1
fib(2) # => 1
fib(3) # => 2
fib(4) # => 3
...

'''
def fib(n):
	if n <= 0:
		return 0

	if n == 1:
		return 1

	return fib(n-2) + fib(n-1)

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3