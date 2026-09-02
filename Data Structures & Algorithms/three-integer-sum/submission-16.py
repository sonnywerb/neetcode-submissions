class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         # we can use the two pointer technique again
         # sort the list
         # go through list with i,
         # set l = i + 1 and r = len(nums) - 1
         # l + 1 if sum of i + l + r < 0
         # r - 1 if sum > 0

        res = []
        nums.sort()
        print(nums)

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1 

                    while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res
