'''
Given a string containing just the characters of
'{', '}', '(',')','[',']'
determine if the input is valid if:
  1. open braces must be closed by the same type of braces
  2. open brace must closed in correct order
Example:
    input: "()"  :returns True
    input: "()[]{}"    :returns True
    input:  "(]"     :returns False
    input:  "([)]"    :returns False
    input:  "([])"     :returns True
'''

given = "{}{()}" #"({[}])"

def get_hashmap():
    hashmap = {}
    hashmap['('] = ')'
    hashmap['{'] = '}'
    hashmap['['] = ']'
    return hashmap


def isValid_braces(given):
    openings = ['(', '[', '{']
    hashmap = get_hashmap()
    stack = []
    for i, val in enumerate(given):
        if given[i] in openings:
            stack.append(given[i])
        if given[i] not in openings:
            check_char = stack[len(stack)-1]
            if given[i] != hashmap[check_char]:
                return False
            else:
                stack.pop(len(stack)-1)
    return True


res = isValid_braces(given)
print(res)