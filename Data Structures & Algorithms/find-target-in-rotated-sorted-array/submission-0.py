class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        left = 0
        right = n-1

        while(left<=right):
            if left == right:
                return left if nums[left] == target else -1
            
            mid = left + int((right-left)/2)

            if(nums[mid] == target):
                return mid
            
            # check if nums[mid] <=nums[right] this means this is completely ascending

            if nums[mid]<=nums[right]:
                if(nums[mid]< target and target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if(nums[left] <= target and target < nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1


        