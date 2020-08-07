'''
Given a binary, the function should return the count of 1
eg: bin(3) = 2 because, 3 is 0b11
    bin(7) = 3 because, 8 is 0b111
'''

bin_val = '0011110011111'


def count_one(bin_val):
    max_ones = 0
    prev = 0
    tmp_cache = []
    for i in range(len(bin_val)):
        if bin_val[i] == "1" and prev == bin_val[i]:
            tmp_cache.append(bin_val[i])
        elif bin_val[i] == "1":
            tmp_cache = []
            tmp_cache.append(bin_val[i])
            prev = bin_val[i]
        else:
            prev = bin_val[i]
            max_ones = max(max_ones, len(tmp_cache))
    return max(max_ones, len(tmp_cache))

val = count_one(bin_val)
print(val)