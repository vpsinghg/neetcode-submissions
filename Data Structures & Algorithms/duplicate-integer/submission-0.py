class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in hash_map:
                return True
            hash_map[nums[i]] = i
        return False
