class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            found = nums[mid]
            if found == target:
                return mid
            if found < target:
                l += 1
            else:
                r -= 1

        return -1