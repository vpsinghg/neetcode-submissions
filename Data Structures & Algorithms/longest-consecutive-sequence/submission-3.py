class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0
        pos_idx = {}

        for idx, num in enumerate(nums):
            pos_idx[num] = idx
        
        largest = 0
        seen = set()
        for idx, num in enumerate(nums):
            if num in seen:
                continue
            x = num
            i = idx
            curr = 1
            largest = max(largest, curr)
            seen.add(num)
            while(x+1 in pos_idx):
                curr += 1
                largest = max(largest, curr)
                x = x + 1
                seen.add(x)

        return largest


        