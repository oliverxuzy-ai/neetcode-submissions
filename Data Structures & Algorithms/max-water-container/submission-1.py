class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # min(l,r) * (r - l)

        # * 6
        # 6 - 1

        l, r = 0, len(heights) - 1

        max_water = 0

        while l < r:
            temp_water = min(heights[l], heights[r]) * (r - l)

            max_water = max(max_water, temp_water)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
            



        return max_water