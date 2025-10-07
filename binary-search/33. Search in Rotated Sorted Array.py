from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            # find the sorted half
            if nums[m] == target:
                return m
            if nums[l] > nums[m]:
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

        return -1


sol = Solution()
print(sol.search([0, 1, 2, 3, 4], 3), 3)
print(sol.search([0, 1, 2, 3, 4], 0), 0)

print(sol.search([3, 4, 5, 0, 1, 2], 4), 1)
print(sol.search([3, 4, 5, 0, 1, 2], 1), 4)

print(sol.search([2, 3, 4, 5, 0, 1], 0), 4)
print(sol.search([2, 3, 4, 5, 0, 1], 3), 1)


print(sol.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
print(sol.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
print(sol.search([1], 0), -1)
print(sol.search([1], 1), 0)
print(sol.search([3, 5, 1], 3), 0)
print(sol.search([3, 5, 1], 1), 2)
print(sol.search([3, 5, 1], 5), 1)
print(sol.search([3, 6, 7], 5), -1)
