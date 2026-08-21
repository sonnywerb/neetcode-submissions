class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # target - nums[i] = nums[j]
        # if nums[j] in seen return nums[j], nums[i]

        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]
            
            seen[nums[i]] = i

        return []
