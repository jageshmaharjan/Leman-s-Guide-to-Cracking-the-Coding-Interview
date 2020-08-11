'''
Find First and Last Position of Element in Sorted Array
eg: [1,3,3,3,5,5,6,6,6,8,9,9], target = 6
  return [4,6]
'''

def first_last_pos(arr, x, s, e):
    if (len(arr) == 1) and (arr[0] == x):
        return [1, 1]
    if (len(arr) == 1) and (arr[0] != x):
        return [-1, -1]
    mid = (s+e)//2
    if arr[mid] == x:
        i = mid
        j = mid
        while (i > -1 ) and (arr[i] == x):
            i -= 1
        while (j < len(arr)) and (arr[j] == x):
            j += 1
        return [i+1, j-1]
    else:
        if arr[mid] > x:
            return first_last_pos(arr, x, s, mid-1)
        elif arr[mid] < x:
            return first_last_pos(arr, x, mid+1, e)


given = [1,3,3,3,5,5,6,6,6,6,8,9]
x = 6
res = first_last_pos(given, x, 0, len(given)-1)
print(res)

