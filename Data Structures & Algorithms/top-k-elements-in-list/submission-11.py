class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        create map of num frequency
        put numbers into buckets
        starting from end of bucket return top k elements
        '''
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in range(len(buckets[i])):
                if len(res) == k:
                    return res
                res.append(buckets[i][j])
        return res