class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set to keep track of unique characters
        # use l, r pointer for window
        # expand window if char not in set
        # while char is in set, shrink window
        longest = 0
        chars = set()
        l, r = 0, 0

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        return longest
