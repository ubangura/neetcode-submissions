class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = [0] * len(nums)
        zero_count = 0
        zero_index = -1

        for i, num in enumerate(nums):
            if num:
                product *= num
            else:
                zero_count += 1
                zero_index = i
        
        if zero_count > 1:
            return output

        if zero_count == 1:
            output[zero_index] = product
            return output

        for i in range(len(nums)):
            output[i] = product // nums[i]

        return output