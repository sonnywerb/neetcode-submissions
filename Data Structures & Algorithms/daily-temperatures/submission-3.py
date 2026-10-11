class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                curr_temp = stack.pop()
                res[curr_temp[1]] = i - curr_temp[1]
            stack.append((temperatures[i], i))
        return res
        