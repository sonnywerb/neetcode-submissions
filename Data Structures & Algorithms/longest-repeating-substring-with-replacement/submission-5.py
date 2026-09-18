class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # keeps track of character frequencies
        max_f = 0 # keeps track of max frequency in count
        res = 0 # our return value

        l = 0 # left pointer
        for r in range(len(s)): # right pointer iterates through string
            # put char, freq into count
            count[s[r]] = count.get(s[r], 0) + 1
            # calculate the max frequency
            max_f = max(max_f, count[s[r]])

            # shrink window if length of substring - max_f 
            # (gives # of replacements) exceeds k
            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            # calculate the longest substring
            res = max(res, r - l + 1)
            
        return res