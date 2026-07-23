class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(char.lower() for char in s if char.isalnum())

        left_ptr, right_ptr = 0, len(filtered) - 1

        while left_ptr <= right_ptr:
            if filtered[left_ptr] != filtered[right_ptr]:
                return False
            
            left_ptr += 1
            right_ptr -= 1
        
        return True