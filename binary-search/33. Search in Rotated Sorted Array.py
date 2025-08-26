from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            m = int(l+(r-l)/2)
            if nums[m]==target: return m

            # inside sorted portion
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m+1
                else:
                    r = m-1
            else:
                # inside right sorted portion
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                     l = m+1
        return -1

sol = Solution()
# print(sol.search([0,1,2,3,4], 3) , 3)
print(sol.search([0,1,2,3,4], 0), 0)

# print(sol.search([3,4,5,0,1,2], 4), 1)
# print(sol.search([3,4,5,0,1,2], 1), 4)

# print(sol.search([2,3,4,5,0,1], 0), 4)
# print(sol.search([2,3,4,5,0,1], 3), 1)


# print(sol.search([4,5,6,7,0,1,2], 0), 4)
# print(sol.search([4,5,6,7,0,1,2], 3), -1)
# print(sol.search([1], 0), -1)
# print(sol.search([1],1), 0)
# print(sol.search([3,5,1],3), 0)
# print(sol.search([3,5,1],1), 2)
# print(sol.search([3,5,1],5), 1)
# print(sol.search([3,6,7],5), -1)
