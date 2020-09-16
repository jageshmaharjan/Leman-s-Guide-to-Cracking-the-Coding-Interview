'''
given a sorted 2D matrix, find a given target value
[ [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23 ,30, 34, 50]
]
target = 3

return True
'''

given = [ [1, 3, 5, 7],
          [10, 11, 16, 20],
          [23 ,30, 34, 50] ]

target = 30


def find_target(matrix, target):
    if len(matrix) == 0:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = rows*cols - 1

    while left <= right:
        mid = left + (right-left)//2
        midpoint_element = matrix[mid//cols][mid%cols]
        if midpoint_element == target:
            return "Found"
        elif (midpoint_element > target):
            right = mid-1
        elif (midpoint_element < target):
            left = mid+1
    return "Not Found"


res = find_target(given, target)
print(res)