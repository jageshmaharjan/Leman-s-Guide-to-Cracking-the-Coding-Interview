


def quick_sort(given, min, max):
    if given == None or len(given) == 0:
        return False
    if min > max:
        return False
    mid = min + (max-min)//2
    pivot = given[mid]
    i = min
    j = max
    while (i < j):
        while (given[i] < pivot):
            i += 1
        while (given[j] > pivot):
            j -= 1
        if (i <= j):
            tmp = given[j]
            given[j] = given[i]
            given[i] = tmp
            i += 1
            j -= 1
    if (min < j):
        quick_sort(given, min, j)
    if max > i:
        quick_sort(given, i, max)
    return given


given = [5,4,3,6,7,2,8,1,9] # [9,1,2,8,7,3,5,4,6]  # [3,8,7,5,6,4,2,1]  [3,8,2,5,1,4,7,6]  [5,4,3,6,7,2,8,1,9]
res = quick_sort(given, 0, len(given)-1)
print(res)