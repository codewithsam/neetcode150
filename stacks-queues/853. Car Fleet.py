from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dst = []
        for i, pos in enumerate(position):
            dst.append((pos, speed[i], (target-pos)/speed[i]))
        sorted_dst = sorted(dst, key=lambda item:item[0], reverse=True)
        fleets = 0
        prevtime = float("-inf")
        for i, dst_tuple in enumerate(sorted_dst):
            if dst_tuple[2] > prevtime:
                fleets+=1
                prevtime = dst_tuple[2]
        
        return fleets
            
            

sol = Solution()
print(sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))