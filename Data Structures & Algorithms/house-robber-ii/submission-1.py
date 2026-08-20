class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]

        memo = [[-1]*2 for _ in range(n)]

        def recursive(i, flag) -> int:

            if i >= n or (flag and i == n-1):
                return 0
            
            if memo[i][1 - int(flag)] != -1:
                return memo[i][1 - int(flag)]
            # robb current
            amount_robbed_current_house = nums[i] + recursive(i+2,flag)
            amount_skipped_current_house = recursive(i+1,flag)

            memo[i][1 - int(flag)]= max(amount_robbed_current_house,amount_skipped_current_house)
            return memo[i][1 - int(flag)]
        return max(recursive(0,True), recursive(1,False))
            
            

        



        