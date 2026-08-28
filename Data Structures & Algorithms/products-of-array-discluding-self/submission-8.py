class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n

        pref[0] = 1
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]
        
        suff[n - 1] = 1
        for j in range(n - 2, -1, -1):
            suff[j] = suff[j + 1] * nums[j + 1]

        res = [0] * n
        for k in range(n):
            res[k] = pref[k] * suff[k]

        return res


