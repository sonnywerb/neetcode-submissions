class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # target - nums[i] = nums[j]
        # if nums[j] in seen return nums[j], nums[i]

        seen = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen:
                return [seen[diff], i]
            
            seen[n] = i
