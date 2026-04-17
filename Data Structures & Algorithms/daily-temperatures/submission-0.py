class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        for i, curr_temp in enumerate(temperatures):
            days = 1

            for temp in temperatures[i + 1:]:
                if temp > curr_temp:
                    result[i] = days
                    break
                days += 1

        return result