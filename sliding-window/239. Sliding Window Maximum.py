from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0 or len(nums) == 0: return []
        if k == 1 and len(nums) == 1: return [nums[0]]
        res = []
        deck = deque()
        l, r = 0, 0
        curmax = float("-inf")
        while r < len(nums):
            while deck and deck[-1] < nums[r]:
                deck.pop()
            deck.append(nums[r])
            if r >= k-1:
                res.append(deck[0])
                if nums[l] == deck[0]:
                    deck.popleft()
                l+=1
            r+=1
        return res



sol = Solution()
print(sol.maxSlidingWindow([1,3,1,2,0,5], 3))