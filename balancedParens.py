'''
 *  balancedParens('[](){}'); // true
 *  balancedParens('[({})]');   // true
 *  balancedParens('[(]{)}'); // false
 *  balancedParens('[(])'); // false
 *  balancedParens(')'); // false
'''

BRACKETS = [('(', ')'), ('[', ']'), ('{','}')]
OPENING_BRACKETS = [x[0] for x in BRACKETS]
CLOSING_BRACKETS = [x[1] for x in BRACKETS]


def balancedParens(query_string):
    """
    query_string: string consisting only of valid BRACKETS characters

    return true if brackets are correctly opened/closed and have proper nesting
    else return false
    """
    stack = []
    for i in range(len(query_string)):
        curr_ele = query_string[i]
        
        if curr_ele in OPENING_BRACKETS:
            stack.append(curr_ele)
            
        else:
            if not stack:
                return False
        
            curr_stack_element = stack.pop()
            
            index = 0
            
            for i in range(len(CLOSING_BRACKETS)):
                if CLOSING_BRACKETS[i] == curr_ele:
                    index = i
                    
            corresponding_open_element = OPENING_BRACKETS[index]
            
            if curr_stack_element != corresponding_open_element:
                return False


    if len(stack)>0:
        return False
    
    return True


assert balancedParens('[](){}') == True
assert balancedParens('[') == False