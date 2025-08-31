'''
This question can be solved with heaps also but we can also do with quick select
Although quick select worst case is O(n)^2 but average case is O(n) since we are always gonna work sorted part of the array
initially we have to sort whole array take 1 element (usually last element) as pivot. 
    - If location of pivot is not equal to k we check if p > k then we sort left side
    - if p < k we sort the right side
    therefore complexity is -> n + n/2 +n/4 +n/8 .... = 2n = n ===> O(n)

REMEMBER: THIS SOLUTION IS NOT ACCEPTED IN LEETCODE BUT DOES NOT MEAN ITS WRONG.
'''

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quickselect(1, p-1)
            elif p < k:
                return quickselect(p+1, r)
            else:
                return nums[p]
        return quickselect(0, len(nums)-1)

sol = Solution()
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6],4))