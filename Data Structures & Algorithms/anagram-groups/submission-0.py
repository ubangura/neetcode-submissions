class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            chars = "".join(sorted(word))
            anagrams.setdefault(chars, []).append(word)
        
        return [value for value in anagrams.values()]