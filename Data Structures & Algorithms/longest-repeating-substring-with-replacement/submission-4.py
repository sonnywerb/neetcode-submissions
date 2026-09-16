class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use a hashmap to keep count of the letter frequency
        # keep track of the most frequent char max_f
        # expand the window while max_f - window size < k
        # if > k, shrink window until it's less
        res = 0
        count = {}
        max_f = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_f = max(max_f, count[s[r]])

            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
