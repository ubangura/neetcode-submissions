class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_ptr = read_ptr = 1

        for read_ptr in range(1, len(nums)):
            curr = nums[read_ptr]

            if curr != nums[read_ptr - 1]:
                nums[write_ptr] = curr
                write_ptr += 1
            
            read_ptr += 1
        
        return write_ptr