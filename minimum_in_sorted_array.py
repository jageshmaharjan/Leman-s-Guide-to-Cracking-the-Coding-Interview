'''
Given a rotatable sorted array, find the minimum value in the array
eg, sorted array is [0,1,2,3,4,5,6,7,8,9] can be rotated as [2,3,4,5,6,7,8,9,0,1] or any number of times.
example, input = [8,9,0,1,2,3,4,5,6,7]
            :returns 1

        input = [15,18,19,3,6,8,9]
        :returns 3
'''

arr =  [1,2,3,4,5,-6,-5,-4,0] #[8,9,0,1,2,3,4,5,6,7]


def min_val_sorted_array(arr):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0]
    left = 0
    right = len(arr) - 1

    while (left <= right):
        midpoint = left + (right - left) // 2
        if arr[midpoint] < arr[midpoint-1]:
            return arr[midpoint]
        elif arr[left] <= arr[midpoint] and arr[midpoint] > arr[right]:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return arr[left]


res = min_val_sorted_array(arr)
print(res)


'''
def findMinRotated(arr, start, end): 
    mid = (end - start) // 2 
    if mid == 0 or arr[mid - 1] > arr[mid]: 
        return arr[mid] 
    if arr[start] < arr[mid]: 
        return findMinRotated(arr, mid, end) 
    return findMinRotated(arr, start, mid) 
    
arr = [15,18,19,-3,6,8,9] 
print(findMinRotated(arr, 0, len(arr) - 1))
'''