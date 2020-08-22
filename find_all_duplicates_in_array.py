'''
Find all duplicates in an array
Given an array of integers, 1<=a[i]<=n (n=size of array),
some elements appears twice while other appears once
find all elements that appears twice in the array.

could you do it without using extra space in O(n) runtime?

example: input [4,3,2,7,8,2,3,1]
            :returns [2,3]
'''
#[1,3,4,2,2] # [4,3,2,7,8,2,3,1]

input = [4,3,2,7,8,2,3,1]

# def find_duplicates(input):
#     duplicates = []
#     for i, val in enumerate(input):
#         idx = abs(val) - 1
#         if input[idx] < 0:
#             duplicates.append(idx + 1)
#         else:
#             input[idx] = -input[idx]
#     return duplicates
#
#
# res = find_duplicates(input)
# print(res)

# === O(1) space and less than O(2^n) ====

def find_duplicates_num(given):
    i = 0
    while i < len(given):
        if i + 1 == given[i]:
            pass
        else:
            if i+1 > given[i]:
                return given[i]
            else:
                if given[given[i]-1] == given[i]:
                    return given[i]
                tmp = given[given[i]-1]
                given[given[i]-1] = given[i]
                given[i] = tmp
                i -= 1
        i += 1


res = find_duplicates_num(input)
print(res)