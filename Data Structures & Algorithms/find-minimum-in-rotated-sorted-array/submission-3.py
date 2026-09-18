class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or (nums[len(nums) - 1] > nums[0]):
            return nums[0]

        l, r = 1, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]