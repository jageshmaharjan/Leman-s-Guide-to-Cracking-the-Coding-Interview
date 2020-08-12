'''
Given a sorted linked list, remove a duplicates

eg: 1->2->2->3->4->4->5
    :returns 1->2->3->4->5
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def get_tree():
    root = Node(1)
    root.next = Node(1)
    root.next.next = Node(2)
    root.next.next.next = Node(2)
    root.next.next.next.next = Node(3)
    root.next.next.next.next.next = Node(4)
    root.next.next.next.next.next.next = Node(4)
    root.next.next.next.next.next.next.next = Node(5)
    return root

root = get_tree()

def remove_duplicates(root):
    values = []
    while root != None:
        if root.val not in values:
            values.append(root.val)
        root = root.next

    new_node = Node(0)
    tmp = new_node
    for val in values:
        tmp.next = Node(val)
        tmp = tmp.next
    return new_node.next

res = remove_duplicates(root)
print(res)


def rmv_dup(root):
    dummy = Node(0)
    tmp = dummy
    prev = -1
    while root != None:
        if root.val != prev:
            tmp.next = root
            tmp = tmp.next
        prev = root.val
        root = root.next
    return dummy.next

result = rmv_dup(root)
print(result)