class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        max_left_so_far = 0
        max_right_so_far = 0
        for i in range(len(height) - 1):
            max_left_so_far = max(height[i], max_left_so_far)
            max_right_so_far = max(height[len(height) - i - 1], max_right_so_far)
            max_left[i + 1] = max_left_so_far
            max_right[len(height) - i - 2] = max_right_so_far

        accumulated = 0
        for i, column in enumerate(height):
            accumulated += max((min(max_left[i], max_right[i]) - column), 0)

        return accumulated

