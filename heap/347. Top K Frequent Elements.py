from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[]]*(len(nums)+1)
        res = []
        map = {}
        for num in nums:
            map[num] = 1+map.get(num, 0)
        print(map)
        for item, freq in map.items():
            bucket[freq] = [*bucket[freq], item]
        for it in bucket[::-1]:
            for i in it:
                res.append(i)
                if len(res) >= k:
                    return res

            

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))