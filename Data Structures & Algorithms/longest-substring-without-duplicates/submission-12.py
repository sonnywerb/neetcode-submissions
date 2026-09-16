class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we will have a set to keep track of the duplicate characters
        # using left and right points, we can expand the window
        # if we encounter a duplicate, we move l to r to shrink the window and 
        # continue
        res = 0
        char_set = set()
        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            res = max(res, r - l + 1)
            char_set.add(s[r])
        return res 