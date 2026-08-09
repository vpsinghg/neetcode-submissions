class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp_1 = curMax * num
            tmp_2 = curMin * num
            curMax = max(tmp_1, tmp_2, num)
            curMin = min(tmp_1, tmp_2, num)
            res = max(res, curMax)
        return res