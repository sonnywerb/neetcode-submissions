class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # create counts for s1 and s2
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # check how many matches the first window has
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        
        # loop through remaining string using sliding windows to check for matches
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # expands window by 1
            right_index = ord(s2[r]) - ord('a')
            s2_count[right_index] += 1
            if s1_count[right_index] == s2_count[right_index]:
                matches += 1
            elif s1_count[right_index] + 1 == s2_count[right_index]:
                matches -= 1
            
            left_index = ord(s2[l]) - ord('a')
            s2_count[left_index] -= 1
            if s1_count[left_index] == s2_count[left_index]:
                matches += 1
            elif s1_count[left_index] - 1 == s2_count[left_index]:
                matches -= 1
            l += 1
        
        return matches == 26
