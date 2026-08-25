class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # essentially we want to add the frequency count
        # as the key in a hashmap
        # then have every word that matches that freq count to
        # be in a list of values
        # then we can just return the entire hashmap values as a list

        # main dictionary
        result = defaultdict(list)

        for word in strs:
            # array to keep track of letter frequency
            count = [0] * 26

            for char in word:
                index = (ord(char) - ord('a'))
                count[index] += 1
            result[tuple(count)].append(word)
        
        return list(result.values())

