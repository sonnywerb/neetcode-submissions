class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if (n - 1) not in nums_set:
                length = 1
                while (n + length) in nums_set:
                    length += 1
                longest = max(longest, length)
        return longest

        # we used a hashset to allow for O(1) looks ups as we iterate through array
        # only start building the consecutive sequence if the current number is
        # the beginning of the sequence (checked by n - 1 where n is the current number)