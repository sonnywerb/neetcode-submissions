class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        letter_counts = defaultdict(list)
        result = []

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
        
            count_tuple = tuple(count)

            letter_counts[count_tuple].append(s)
        
        return list(letter_counts.values())


        
        