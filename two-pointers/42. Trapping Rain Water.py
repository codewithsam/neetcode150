from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight, total_water = 0, 0, 0
        while l < r:
            if height[l] <= height[r]:
                if height[l] > maxLeft:
                    maxLeft = height[l]
                else:
                    total_water += max(0, maxLeft - height[l])
                l += 1
            else:
                if height[r] > maxRight:
                    maxRight = height[r]
                else:
                    total_water += max(0, maxRight - height[r])
                r -= 1
        return total_water


sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(sol.trap([4, 2, 0, 3, 2, 5]))  # 9
