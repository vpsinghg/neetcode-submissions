class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        minimum = nums[0]

        while(left<=right):
            mid = (left + (right-left)//2)

            # check if which part is sorted
            minimum = min(minimum,nums[mid])
            if nums[left] <= nums[mid]:
                minimum = min(minimum,nums[left])
                left=mid+1
            else:
                right=mid-1
        
        return minimum