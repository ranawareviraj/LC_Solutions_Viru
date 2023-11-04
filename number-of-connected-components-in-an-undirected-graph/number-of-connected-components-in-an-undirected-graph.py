class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n

    # The function to find root
    def find(self, node):
        if self.root[node] == node:
            return node
        return self.find(self.root[node])

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if self.rank[root_x] > self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.root[root_x] = root_y
        self.rank[root_y] += self.rank[root_x]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        for (x, y) in edges:
            union_find.union(x, y)
        
        roots = set()
        for node in range(n):
            roots.add(union_find.find(node))

        return len(roots)