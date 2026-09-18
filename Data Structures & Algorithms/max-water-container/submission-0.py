class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        l, r = 0, len(heights) - 1

        while l < r:
            lh = heights[l]
            rh = heights[r]
            current_volume = min(lh, rh) * (r - l)

            if lh <= rh:
                l += 1
            else:
                r -= 1

            max_water = max(current_volume, max_water)

        return max_water
