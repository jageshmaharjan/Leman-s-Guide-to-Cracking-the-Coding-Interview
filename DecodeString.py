'''
Given an encoded string, return its decoded string
examples: s = "3[a]2[bc]"  :returns "aaabcbc"
          s = "3[a2[c]]"  :returns "accacc"
          s= "2[abc]3[cd]ef"  :returns "abcabccdcdcdef"
'''

given = "2[ab2[z3[x]]c]3[cd]ef" #"3[a2[c]]"  #"2[abc]3[cd]ef" #2[ab2[z3[x]]c]3[cd]ef


def decode_string(given):
    prev_pos = -1
    for i, char in enumerate(given):
        if char == '[':
            prev_pos = i
        if char == ']':
            val = given[prev_pos+1:i]
            tmp = ''
            times = int(given[prev_pos-1])
            for _ in range(times):
                tmp += val
            return decode_string(given.replace(given[prev_pos-1:i+1], tmp))
    return given


res = decode_string(given)
print(res)

