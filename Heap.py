import math

# You cannot add any items to the heap after you start deleting the node

# Recursive way
def check_bubble_up(nodelst, index):
    if index == 0:
        return True
    parent = math.floor(index/2)
    if nodelst[parent] > nodelst[index]:
        tmp = nodelst[index]
        nodelst[index] = nodelst[parent]
        nodelst[parent] = tmp
    check_bubble_up(nodelst, parent)
    return True

# iterative way
# def check_bubble_up(nodelst, index):
#     while index != 0:
#         parent = math.floor(index/2)
#         if nodelst[parent] > nodelst[index]:
#             tmp = nodelst[index]
#             nodelst[index] = nodelst[parent]
#             nodelst[parent] = tmp
#         index = parent
#     return True


def check_min_index(nodelst, child_index_1, child_index_2):
    if nodelst[child_index_1] >= nodelst[child_index_2]:
        return child_index_2
    if nodelst[child_index_1] < nodelst[child_index_2]:
        return child_index_1


def check_bubble_down(nodelst, cur_idx, last_idx):
    if last_idx == cur_idx:
        return True
    child_index_1 = 2 * cur_idx + 1
    child_index_2 = 2 * cur_idx + 2
    if (child_index_1 >= last_idx) and (child_index_1 > last_idx):
        return True
    if (child_index_1 <= last_idx) and (child_index_1 >= last_idx):
        min_idx = child_index_1
        if nodelst[cur_idx] > nodelst[min_idx]:
            tmp = nodelst[cur_idx]
            nodelst[cur_idx] = nodelst[min_idx]
            nodelst[min_idx] = tmp
        check_bubble_down(nodelst, min_idx, last_idx)
    else:
        min_idx = check_min_index(nodelst, child_index_1, child_index_2)
        if nodelst[cur_idx] > nodelst[min_idx]:
            tmp = nodelst[cur_idx]
            nodelst[cur_idx] = nodelst[min_idx]
            nodelst[min_idx] = tmp
        check_bubble_down(nodelst, min_idx, last_idx)


class Heap:
    def __init__(self):
        self.nodelst = []
        self.last_pos = -1

    def add_node(self, node):
        self.nodelst.append(node)
        self.last_pos += 1
        check_bubble_up(self.nodelst, len(self.nodelst)-1)

    def delete_node(self):
        heap_size = len(self.nodelst)
        if heap_size != 0:
            tmp = self.nodelst[0]
            self.nodelst[0] = self.nodelst[self.last_pos]
            self.nodelst[self.last_pos] = tmp
        self.last_pos -= 1
        check_bubble_down(self.nodelst, 0, self.last_pos)


heap = Heap()
nodes = [4,5,3,6,5,8,2,1]
for node in nodes:
    heap.add_node(node)
for i in range(len(nodes)):
    heap.delete_node()
print(heap.nodelst)