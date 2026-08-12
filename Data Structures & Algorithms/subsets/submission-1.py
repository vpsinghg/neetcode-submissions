class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        subset_size = 2**n
        res = []

        for i in range(subset_size):
            x = i
            subset = []
            for j in range(n):
                if x & 1:
                    subset.append(nums[j])
                x = x >> 1
            
            res.append(subset)
        
        return res

        