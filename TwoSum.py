'''
given an array of integers,
return the indices so that their values adds up to target.
example: array = [2, 7, 11, 15]   target = 9
         :return [0, 1]
'''

given = [2, 3, 7, 11, 15]
target = 14

# def two_sum(arr, trgt):
#     for i, val in enumerate(arr):
#         if (trgt-val) in arr:
#             idx = arr.index((trgt-val))
#             return [i, idx]
#     return None


def two_sum(arr, trgt):
    hashmap = {}
    for i, val in enumerate(arr):
        required = trgt - val
        if required in hashmap:
            idx = hashmap[required]
            return [idx, i]
        hashmap[val] = i
    return None


res = two_sum(given, target)
print(res)
