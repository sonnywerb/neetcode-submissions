class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] 

        for i, t in enumerate(temperatures):
            # while stack is not empty and
            # the temperature is greater than previous
            # day's temperatures
            while stack and t > stack[-1][0]:
                # remove the prev day's temp, index
                stackT, stackIdx = stack.pop()\
                # calculate the days between the warmer day
                # and prev days and update res
                res[stackIdx] = i - stackIdx
            stack.append((t, i))
        return res

