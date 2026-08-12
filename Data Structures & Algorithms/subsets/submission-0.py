class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]] # empty

        for num in nums:
            size = len(res)
            for subset in range(size):
                tmp = res[subset].copy()
                tmp.append(num)
                res.append(tmp)
        
        return res;
        