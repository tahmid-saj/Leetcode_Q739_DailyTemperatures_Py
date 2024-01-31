class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stk = [0] * len(temperatures), []
        for i in range(0, len(temperatures)):

            while len(stk) != 0 and stk[-1][0] < temperatures[i]:
                idx = stk.pop()[1]
                res[idx] = i - idx
            stk.append((temperatures[i], i))

        return res
