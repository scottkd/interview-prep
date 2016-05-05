# Live Coding Challenge - Blend Labs

# Given an ordered list of (inclusive) disjoint integer ranges and an integer range, write a function that will merge the range into the list
# such that the resulting list is also an ordered list of disjoint integer ranges.

# (1,2), [] => [(1,2)]
# (1,4), [(-1,3), (7,10)] => [(-1,4), (7,10)]
# (30,40), [(2,3), (7,8), (100,200)] => [(2,3), (7,8), (30,40), (100,200)]
# (3,40), [(2,3), (7,8), (100,200)] => [(2,40), (100,200)]

def merge(input_tuple, tuple_list):
    return_list = []
    low_input = input_tuple[0]
    high_input = input_tuple[1]
    if not tuple_list:
        return_list.append(input_tuple)
    else:
        to_add = [low_input, high_input]
        for i in range(len(tuple_list)):
            curr_tuple = tuple_list[i]
            
            if to_add[0] > curr_tuple[1]:
                return_list.append(curr_tuple)
                
            elif to_add[1] < curr_tuple[0]:
                return_list.append(tuple(to_add))
                return_list += tuple_list[i:]  # check off by one
                return return_list
            
            else:
                to_add[0] = min(to_add[0], curr_tuple[0])
                to_add[1] = max(to_add[1], curr_tuple[1])
                
        return_list.append(tuple(to_add))
            
    return return_list

assert merge((1,2), []) == [(1,2)]
assert merge((1,4), [(-1,3), (7,10)]) == [(-1,4), (7,10)]
assert merge((30,40), [(2,3), (7,8), (100,200)]) == [(2,3), (7,8), (30,40), (100,200)]
assert merge((3,40), [(2,3), (7,8), (100,200)]) == [(2,40), (100,200)]
assert merge((1,2), [(3,4)]) == [(1,2), (3,4)]
assert merge((1,10), [(-10,-2), (3,4), (5,7)]) == [(-10, -2), (1, 10)]
assert merge((1,4) , [(-1,3), (7,10)]) == [(-1, 4), (7, 10)]
assert merge((1,2) , [(2,3), (6,8), (100, 200)]) == [(1, 3), (6, 8), (100, 200)]
assert merge((5,10) , [(2,3), (6,8), (100, 200)]) == [(2, 3), (5, 10), (100, 200)]
assert merge((7,150) , [(2,3), (6,8), (100, 200)]) == [(2, 3), (6, 200)]
assert merge((1,2) , []) == [(1, 2)]
assert merge((10,20) , [(2,3), (4,8), (100, 200)]) == [(2, 3), (4, 8), (10, 20), (100, 200)]
