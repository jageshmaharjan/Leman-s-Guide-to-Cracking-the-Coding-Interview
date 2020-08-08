
def mergesort(array, i, l):
    if array == []:
        return False
    if len(array) == 2:
        if array[0] > array[1]:
            tmp = array[0]
            array[0] = array[1]
            array[1] = tmp
            return array
        else:
            return array
    if len(array) == 1:
        return array
    else:
        mid = (i + len(array))//2
        return merge(mergesort(array[i:mid], i, mid), mergesort(array[mid:l], i, mid+1))


def merge(arr1, arr2):
    if (arr1 != None) or (arr2 != None):
        new_arr = []
        i = 0
        j = 0
        while ((i < len(arr1)) and (j < len(arr2))):
            if (arr1[i] > arr2[j]):
                new_arr.append(arr2[j])
                j += 1
                if j >= len(arr2):
                    while(i < len(arr1)):
                        new_arr.append(arr1[i])
                        i += 1
            elif arr1[i] <= arr2[j]:
                new_arr.append(arr1[i])
                i += 1
                if i >= len(arr1):
                    while (j < len(arr2)):
                        new_arr.append(arr2[j])
                        j += 1
        return new_arr


given = [9,7,4,15,6,2,8,3,1]
print(mergesort(given, 0, len(given)))