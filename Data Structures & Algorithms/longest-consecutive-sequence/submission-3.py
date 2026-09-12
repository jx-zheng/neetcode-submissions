class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        curr_longest = 0
        curr = 1

        for num in nums:
            if num - 1 in num_set:
                continue
            
            next_num = num + 1
            while next_num in num_set:
                curr += 1
                next_num += 1
            
            curr_longest = max(curr_longest, curr)
            curr = 1


        return curr_longest
