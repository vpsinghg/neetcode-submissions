class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0

        n = len(nums)

        if n == 1:
            return nums[0]
        
        prev1 = 0
        prev2 = 0

        for num in nums:
            rob = max(prev1 + num,prev2)
            prev1 = prev2
            prev2 = rob
        
        return prev2