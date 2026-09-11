class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 4, 6]

        #before array: [1, 1, 2, 8]
        #after array: [48, 24, 6, 1]
        #product: 48, 24, 12, 8

        before_array = [1] * len(nums)
        after_array = [1] * len(nums)
        ret = []

        for i in range(1, len(nums)):
            before_array[i] = before_array[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            after_array[i] = after_array[i + 1] * nums[i + 1]

        #print(before_array)
        #print(after_array)

        for i, j in zip(before_array, after_array):
            ret.append(i * j)

        return ret
