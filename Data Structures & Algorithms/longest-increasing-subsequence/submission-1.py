class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def backtrack(index):
            if index in memo:
                return memo[index]

            if index == n - 1:
                return 1

            maxi = 1

            for i in range(index + 1, n):
                if nums[i] > nums[index]:
                    maxi = max(maxi, 1 + backtrack(i))

            memo[index] = maxi
            return maxi

        ans = 0

        for i in range(n):
            ans = max(ans, backtrack(i))

        return ans