class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 # length we're returning
        chars = set() # set to keep track of the letters

        l = 0
        for r in range(len(s)):
            # shrink window while we have duplicates
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            # add letter to set
            chars.add(s[r])
            res = max(res, r - l + 1)
        
        return res