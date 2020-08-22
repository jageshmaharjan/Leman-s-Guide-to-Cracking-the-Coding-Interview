'''Tree Traversal of the Given tree
          1
        /   \
       2     3
      / \   /
     4   5 6
'''

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right= right

def get_tree():
    n1 = Node(6, None, None)
    n2 = Node(5, None, None)
    n3 = Node(4, None, None)
    n4 = Node(2, n3, n2)
    n5 = Node(3, n1, None)
    n6 = Node(1, n4, n5)
    return n6

n = get_tree()

def post_order_traversal(n, cache):
    if n == None:
        return True
    post_order_traversal(n.left, cache)
    post_order_traversal(n.right, cache)
    cache.append(n.name)

print("Post Order Tree Traversal")
cache = []
post_order_traversal(n,cache)
print(cache)

def in_order_traversal(n, cache):
    if n == None:
        return True
    in_order_traversal(n.left, cache)
    cache.append(n.name)
    in_order_traversal(n.right, cache)

print("In Order Tree Traversal")
cache = []
in_order_traversal(n, cache)
print(cache)

def pre_order_traversal(n, cache):
    if n == None:
        return True
    cache.append(n.name)
    pre_order_traversal(n.left, cache)
    pre_order_traversal(n.right, cache)

print("Pre Order Tree Traversal aks DFS")
cache = []
pre_order_traversal(n, cache)
print(cache)


def dfs(n, visited, cache):
    if n == None:
        return True
    if n not in visited:
        cache.append(n.name)
        visited.append(n.name)
        dfs(n.left, visited, cache)
        dfs(n.right, visited, cache)

print("DFS")
visited = []
cache = []
dfs(n, visited, cache)
print(cache)

def bfs(n, q):
    if n == None:
        return False
    s = []
    s.append(n.name)
    q.append(n)
    while len(q) != 0:
        v = q[0]
        q.remove(v)
        if (v.left != None) and (v.left.name not in s):
            s.append(v.left.name)
            q.append(v.left)
        if (v.right != None) and (v.right.name not in s):
            s.append(v.right.name)
            q.append(v.right)
    return s


print("BFS")
q = []
print(bfs(n, q))