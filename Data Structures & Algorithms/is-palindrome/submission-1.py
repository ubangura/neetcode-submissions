class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr, right_ptr = 0, len(s) - 1

        while left_ptr <= right_ptr:
            left = s[left_ptr]
            right = s[right_ptr]

            if not left.isalnum():
                left_ptr += 1
                continue
            if not right.isalnum():
                right_ptr -= 1
                continue
            
            if left.lower() != right.lower():
                return False
            
            left_ptr += 1
            right_ptr -= 1

        return True