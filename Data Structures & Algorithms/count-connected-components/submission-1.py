class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node: int):
        curr = node

        while curr != self.parent[curr]:
            curr = self.parent[curr]

        return curr

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pv == pu:
            return False

        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res
