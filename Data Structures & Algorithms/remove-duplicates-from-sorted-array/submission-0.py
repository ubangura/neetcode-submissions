class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Init left_ptr to index 0; right_ptr to index 1
        left_ptr, right_ptr = 0, 1

        # Time complexity: O(n)
        # while right_ptr < len(nums)
            # Is nums[left] == nums[right]
                # Yes: pop nums[right]
                # No: increment left and right ptr
        while right_ptr < len(nums):
            if nums[left_ptr] == nums[right_ptr]:
                nums.pop(right_ptr)
                continue
            
            left_ptr += 1
            right_ptr += 1
        
        # return len(nums)
        return len(nums)