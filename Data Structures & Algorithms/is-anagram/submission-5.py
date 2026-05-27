class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_freq_s = {}
        char_freq_t = {}

        for i in range(len(s)):
            char_freq_s[s[i]] = 1 + char_freq_s.get(s[i], 0)
            char_freq_t[t[i]] = 1 + char_freq_t.get(t[i], 0)
        
        return char_freq_s == char_freq_t
        