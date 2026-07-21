class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected_sum=int((n*(n+1))/2)
        current_sum = sum(num for num in nums)
        return expected_sum - current_sum;
        