class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, count = 0, 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            count = max(count , right-left+1)
        return count
    
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))