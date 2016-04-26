"""
A crack team of love scientists from OkEros (a hot new dating site) have devised a way to represent dating profiles as rectangles on a two-dimensional plane.
They need help writing an algorithm to find the intersection of two users' love rectangles. They suspect finding that intersection is the key to a matching algorithm so powerful it will cause an immediate acquisition by Google or Facebook or Obama or something.

It must
be love
Write a function to find the rectangular intersection of two given love rectangles.

As with the example above, love rectangles are always "straight" and never "diagonal." More rigorously: each side is parallel with either the x-axis or the y-axis.

They are defined as dictionaries like this:
 
my_rectangle = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,

}
rect1 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,
}

Your output rectangle should use this format as well.
"""
no_overlap_dict = {
	'left_x':0,
	'bottom_y':0,
	'width':0,
	'height':0,
}
def find_intersection(rectangles):
	return_dict = {
		'left_x':0,
		'bottom_y':0,
		'width':0,
		'height':0,
	}

	# find x overlap
	if rectangles[0]['left_x'] <= rectangles[1]['left_x']:
		left_rectangle = rectangles[0]
		right_rectangle = rectangles[1]
	else:
		left_rectangle = rectangles[1]
		right_rectangle = rectangles[0]

	if left_rectangle['left_x'] + left_rectangle['width'] < right_rectangle['left_x']:
		return no_overlap_dict
	
	else:
		left_x = max(left_rectangle['left_x'], right_rectangle['left_x'])
		right_x = min(left_rectangle['left_x'] + left_rectangle['width'], right_rectangle['left_x'] + right_rectangle['width']) 
		return_dict['left_x'] = left_x
		return_dict['width'] = right_x - left_x

	# find y overlap
	if rectangles[0]['bottom_y'] <= rectangles[1]['bottom_y']:
		bottom_rectangle = rectangles[0]
		top_rectangle = rectangles[1]
	else:
		bottom_rectangle = rectangles[1]
		top_rectangle = rectangles[0]

	if bottom_rectangle['bottom_y'] + bottom_rectangle['height'] < top_rectangle['bottom_y']:
		return no_overlap_dict
	
	else:
		bottom_y = max(bottom_rectangle['bottom_y'], top_rectangle['bottom_y'])
		top_y = min(bottom_rectangle['bottom_y'] + bottom_rectangle['height'], top_rectangle['bottom_y'] + top_rectangle['width']) 
		return_dict['bottom_y'] = bottom_y
		return_dict['height'] = top_y - bottom_y

	if return_dict['width'] == 0 or return_dict['height'] == 0:
		return no_overlap_dict

	return return_dict

d1 = {
	'left_x':0,
	'bottom_y':0,
	'width':5,
	'height':5,
}
d2 = {
	'left_x':1,
	'bottom_y':1,
	'width':5,
	'height':5,
}
d3 = {
	'left_x':5,
	'bottom_y':5,
	'width':5,
	'height':5,
}
d4 = {
	'left_x':10,
	'bottom_y':10,
	'width':10,
	'height':10,
}
d5 = {
	'left_x':-1,
	'bottom_y':-1,
	'width':2,
	'height':2,
}


assert find_intersection([d1, d2]) == {'left_x':1, 'bottom_y':1, 'width':4, 'height':4}
assert find_intersection([d1, d3]) == {'left_x':0, 'bottom_y':0, 'width':0, 'height':0}
assert find_intersection([d1, d4]) == {'left_x':0, 'bottom_y':0, 'width':0, 'height':0}
assert find_intersection([d5, d1]) == {'left_x':0, 'bottom_y':0, 'width':1, 'height':1}