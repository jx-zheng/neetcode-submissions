class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            #if not stack:
            #    stack.append( (temperature, i) )
            #    continue
            
            while stack and stack[-1][0] < temperature:
                colder_index = stack.pop()[1]
                ret[colder_index] = i - colder_index

            stack.append( (temperature, i) )

        return ret
        