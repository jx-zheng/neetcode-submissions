class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        running_count = 0
        for num in range(len(nums) + 1):
            running_count = running_count ^ num
        
        for num in nums:
            running_count = running_count ^ num

        return running_count
