class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        
        have, need = 0, len(count)
        res = [-1, -1]
        res_len = float('inf')
        window = {}
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in count and window[c] == count[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        
        return s[l : r + 1] if res_len != float('inf') else ""
        