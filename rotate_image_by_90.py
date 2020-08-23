'''
Given an array of 2D of size n x n also known as image.
rotate an image by 90 degree clockwise
Note: You have to rotate an image in-place, no extra space is allowed.

[1,2,3         [ 7,4,1
 4,5,6     =>    8,5,2
 7,8,9           9,6,3
]              ]

'''

# array = [[1,2,3],[4,5,6],[7,8,9]]
array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def rotate_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if i != j and j >i:
                tmp = array[i][j]
                array[i][j] = array[j][i]
                array[j][i] = tmp


    for i in range(len(array)):
        p = len(array[0]) - 1
        for j in range(len(array[0])):
            if j < p:
                tmp = array[i][j]
                array[i][j] = array[i][p]
                array[i][p] = tmp
            p -= 1
    return array

print(rotate_array(array))