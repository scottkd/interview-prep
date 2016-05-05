'''
I want to learn some big words so people think I'm smart.
I opened up a dictionary to a page in the middle and started flipping through, looking for words I didn't know. I put each word I didn't know at increasing indices in a huge list I created in memory. When I reached the end of the dictionary, I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an alphabetically ordered list that has been "rotated." For example:

  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

Write a function for finding the index of the "rotation point," which is where I started working from the beginning of the dictionary. This list is huge (there are lots of words I don't know) so we want to be efficient here.
'''
def find_rotation_point(words):
	'''Implementation assumes there MUST be a rotation in data. words cannot be an order list.'''
	return find_rotation_helper(words, 0, len(words) - 1)

def find_rotation_helper(words, start, end):
	if end - start == 1:						# If we are down to two indices, choose correct index
		if words[start] > words[end]:
			return end
		else:
			return start

	mid = (end + start) / 2								# set midpoint

	if words[mid] > words[start]:						# search upper half
		return find_rotation_helper(words, mid, end)

	elif words[mid] < words[start]:
		return find_rotation_helper(words, start, mid)	# search lower half


words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

w2 = ['b', 'c', 'a']

w3 = ['z', 'a', 'b', 'c', 'd']

assert find_rotation_point(words) == 5, find_rotation_point(words)
assert find_rotation_point(w2) == 2, find_rotation_point(w2)
assert find_rotation_point(w3) == 1, find_rotation_point(w3)
