class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}

        for i, num in enumerate(nums):
            target_pairing = target - num
            if num in sum_map:
                return [sum_map[num], i]
            sum_map[target_pairing] = i