class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        # calculate prefix product
        prefix = [1]
        for i in range(0, n - 1):
            prefix.append(prefix[i] * nums[i])

        # calculate suffix product
        suffix = [1]
        for j in range(n - 1, 0, -1):
            suffix.append(suffix[n - 1 - j] * nums[j])

        # multiply prefix * suffix
        for m in range(n - 1, -1, -1):
            res.append(suffix[m] * prefix[n - 1 - m])

        return res
