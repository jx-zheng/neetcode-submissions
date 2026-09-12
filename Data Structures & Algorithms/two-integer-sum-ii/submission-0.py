class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            l_num = numbers[l]
            r_num = numbers[r]

            _sum = l_num + r_num
            if _sum == target:
                return [l+1, r+1]
            elif _sum > target:
                r = r - 1
            else:
                l = l + 1

        return False

