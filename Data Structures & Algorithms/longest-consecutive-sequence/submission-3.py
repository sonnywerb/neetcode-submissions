class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest = 0

        for n in nums:
            if (n-1) in nums_set:
                continue
            
            curr = 1
            # n is start of sequence
            while (n+1) in nums_set:
                curr += 1
                n += 1
            longest = max(longest, curr)

        return longest

        # we used a hashset to allow for O(1) looks ups as we iterate through array
        # only start building the consecutive sequence if the current number is
        # the beginning of the sequence (checked by n - 1 where n is the current number)