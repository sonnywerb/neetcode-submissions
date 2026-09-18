class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # it's impossible for a shorter
        # string to contain a larger string
        if len(s1) > len(s2):
            return False
        
        # create frequency array for entire s1
        # and for the first window of s2
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        # create matches array to compare s1 and s2 counts
        matches = 0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)
        
        # sliding window algorithm here
        l = 0
        # notice we are starting at the second window
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True # permutation found
            
            # checking the letters in this current window
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1 # increment char in s2_count
            # if the counts match, increment matches
            if s1_count[index] == s2_count[index]:
                matches += 1
            # counts don't match, s2_count has a higher char count
            # decrement matches
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1
            
            # preparing to shrink the window 
            # removes char at left side of window
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            l += 1
        
        # s1_count must == s2_count for matches == 26
        return matches == 26

