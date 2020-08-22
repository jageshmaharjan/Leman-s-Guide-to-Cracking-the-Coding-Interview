'''
given an non-empty integer array, return the third max number in the array.
example: input = [1, 2, 3]
            :returns 1
'''

input = [1,2,3]#[1,8,2,5,9,6,3,7]

import sys
class Heap:
    def __init__(self):
        self.f = -sys.maxsize+2
        self.s = -sys.maxsize+1
        self.t = -sys.maxsize
    def add(self, val):
        if val > self.f:
            self.t = self.s
            self.s = self.f
            self.f = val
        elif val < self.f and val > self.s:
            self.t = self.s
            self.s = val
        elif val < self.s and val > self.t:
            self.t = val


def find_third_max(input):
    heap = Heap()
    if len(input) < 3:
        return -1
    for val in input:
        heap.add(val)
    return heap.t

res = find_third_max(input)
print(res)
