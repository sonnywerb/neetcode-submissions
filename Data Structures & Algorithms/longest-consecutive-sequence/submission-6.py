class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # for brute force, we can iterate through and try to build
        # the longest sequence at each number which is O(n^2)
        # instead we can build ONLY when we're at a n we know is the
        # start of the sequence by checking if n-1 is in the list
        # use hashset for O(1) lookup time

        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            curr = 0
            if (n - 1) not in nums_set:
                while (n + curr) in nums_set:
                    curr += 1
            longest = max(curr, longest)
        return longest