'''
            1
          /   \
         2     3
       /  \   / \
      4   5  6   7
            /
           8
'''



class Tree:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

n7 = Tree(7, None, None)
n8 = Tree(8, None, None)
n6 = Tree(6, n8, None)
n3 = Tree(3, n6, n7)
n5 = Tree(5, None, None)
n4 = Tree(4, None, None)
n2 = Tree(2, n4, n5)
n1 = Tree(1, n2, n3)


def helper(root, cache, level):
    if root == None:
        return True

    # if level in cache:
    #     cache[level].append(root.val)
    # else:
    cache[level] = root.val # [root.val]

    helper(root.left, cache, level+1)
    helper(root.right, cache, level+1)
    return cache


def right_side_view(root):
    cache = {}
    return helper(root, cache, 1)

res = right_side_view(n1)
# print(list(res.values()))
print(list(res.values()))