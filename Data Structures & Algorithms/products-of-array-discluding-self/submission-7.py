class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suff = [1] * n

        for i in range(1, n):
            pref[i] = pref[i -1] * nums[i - 1]
        
        for j in range(n - 2, -1, -1):
            suff[j] = suff[j + 1] * nums[j + 1]

        res = []
        for k in range(n):
            res.append(pref[k] * suff[k])

        return res


