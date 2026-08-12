class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(index, curr_sum, curr):
            if index >=len(nums):
                return
            if curr_sum > target:
                return
            
            if curr_sum == target:
                res.append(curr.copy())
                return
            
            # include it
            curr.append(nums[index])
            dfs(index, curr_sum + nums[index], curr) # pick again
            curr.pop()
            dfs(index+1,curr_sum,curr)
            
        dfs(0,0,[])
        return res



                
                

        

        