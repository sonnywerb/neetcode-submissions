class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # calculate prefix product
        prefix = [1]
        for i in range(0, len(nums) - 1):
            prefix.append(prefix[i] * nums[i])

        # calculate suffix product
        suffix = [1]
        for j in range(len(nums) - 1, 0, -1):
            suffix.append(suffix[len(nums) - 1 - j] * nums[j])

        # multiply prefix * suffix
        for n in range(len(suffix) - 1, -1, -1):
            res.append(suffix[n] * prefix[len(suffix) - 1 - n])

        return res
