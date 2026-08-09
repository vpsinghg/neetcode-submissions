class Solution:
    def max_product(self, nums: List[int]) -> int:
        maximum = float("-inf")

        curr = 1
        curr_max_negative = 1
        first_negative = None

        for num in nums:
            curr = curr*num
            curr_max_negative = curr_max_negative*num

            maximum = max(maximum,curr,curr_max_negative)
            if num == 0:
                curr_max_negative = 1
                curr = 1
            elif num<0:
                curr = 1

        return int(maximum)

    def maxProduct(self, nums: List[int]) -> int:
        max_l = self.max_product(nums)
        rev_nums = reversed(nums)
        max_r = self.max_product(rev_nums)

        return max(max_l,max_r)



        