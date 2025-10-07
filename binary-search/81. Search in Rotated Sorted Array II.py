from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2

            # find the sorted half
            if nums[m] == target:
                return True
            # if i am at an edge case where my i cannot detect sorted half then trim down
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1

            elif nums[l] > nums[m]:
                # that means left half is not sorted
                # if we know that left half is unsorted but the right half is sorted
                # in that case check if the target lies between mid and right half
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # that means left half is sorted
                # if left half is sorted and target inside left half then r = m
                # if target is in right half which is unsorted then l = m+1
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return False


sol = Solution()

# 1. Normal sorted array (no rotation, no duplicates)
print(sol.search([0, 1, 2, 3, 4], 3))  # True
print(sol.search([0, 1, 2, 3, 4], 5))  # False

# 2. Rotated array without duplicates
print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))  # True
print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))  # False

# 3. Rotated array with duplicates
print(sol.search([2, 5, 6, 0, 0, 1, 2], 0))  # True
print(sol.search([2, 5, 6, 0, 0, 1, 2], 3))  # False

# 4. Edge case: all elements same
print(sol.search([1, 1, 1, 1, 1], 1))  # True
print(sol.search([1, 1, 1, 1, 1], 2))  # False

# 5. Edge case: pivot surrounded by duplicates
print(sol.search([1, 1, 1, 3, 1], 3))  # True
print(sol.search([1, 1, 1, 3, 1], 2))  # False

# 6. Single element
print(sol.search([1], 1))  # True
print(sol.search([1], 0))  # False
