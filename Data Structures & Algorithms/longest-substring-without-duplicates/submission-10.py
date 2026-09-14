class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set to keep track of unique characters
        # use l, r pointer for window
        # expand window if char not in set
        # while char is in set, shrink window
        longest = 0
        char_set = set()
        l = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
