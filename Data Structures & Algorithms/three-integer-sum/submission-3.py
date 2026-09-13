class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        nums_len = len(nums)
        # [-4, -1, -1, ]
        #print(nums)
        [0, 0, 0, 0]

        left_num_index = 0
        while left_num_index < nums_len - 2:
            if left_num_index > 0 and nums[left_num_index - 1] == nums[left_num_index]:
                left_num_index += 1
                continue
            l, r = left_num_index + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[left_num_index] == 0:
                    triplets.append([nums[l], nums[r], nums[left_num_index]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] + nums[left_num_index] < 0:
                    l += 1
                else:
                    r -= 1
            left_num_index += 1

        return triplets
