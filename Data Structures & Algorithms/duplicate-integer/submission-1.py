class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()

        for i in nums:
            if i not in dupes:
                dupes.add(i)
            else:
                return True
        
        return False
        