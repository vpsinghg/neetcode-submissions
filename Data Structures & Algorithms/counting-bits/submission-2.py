class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [-1 for i in range(n+1)]
        def find_1s(i):
            if i == 0:
                res[i] = 0
                return 0
            if res[i]==-1:
                res[i]=find_1s(i >> 1) + (i & 1)
            return res[i]

        for i in range(0, n + 1):
            find_1s(i)

        return res
