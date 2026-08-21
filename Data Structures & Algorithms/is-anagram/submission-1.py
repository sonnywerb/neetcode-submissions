class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_hashmap = {}
        t_hashmap = {}

        for i in range(len(s)):
            if s[i] not in s_hashmap:
                s_hashmap[s[i]] = 1
            else:
                s_hashmap[s[i]] += 1
            
            if t[i] not in t_hashmap:
                t_hashmap[t[i]] = 1
            else:
                t_hashmap[t[i]] += 1
            
        
        for key in s_hashmap.keys():
            if s_hashmap[key] != t_hashmap.get(key, 0):
                return False
        
        return True



        