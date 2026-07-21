class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)
        for i in range(n):
            compliment = target - nums[i]
            if compliment in hash_map:
                return [hash_map[compliment], i]

            if nums[i] not in hash_map:
                hash_map[nums[i]] = i
