class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # two pointers - l and r
        # make sure numbers[l] != numbers[right]
        # add them, if < target -> increment l
        # if > target, decrement r
        # remember it's 1-indexed
        
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]

            if s == target:
                return [l + 1, r + 1]
            elif s > target:
                r -= 1
            else:
                l += 1
                

        