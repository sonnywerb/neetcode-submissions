class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        # get frequencies of t
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        # indices of substring to return
        res = [-1, -1]
        # min length of valid substring
        min_len = float('inf')

        # keep track of matched character frequencies
        have, need = 0, len(count_t)
        # our sliding window
        window = {}
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1 # expand window

            # if we have matching frequencies increment have
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            # we have a valid substring
            while have == need:
                # check if substring has smaller length than min_len
                if (r - l + 1) < min_len:
                    res = [l, r] # update with new res/min_len
                    min_len = r - l + 1

                # can begin to shrink to find min
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]: # if we shrink and lose our valid substring
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if res != float('inf') else ""

