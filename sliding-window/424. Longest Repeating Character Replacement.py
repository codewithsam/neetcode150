
class Solution:
    def characterReplacement(self, s:str, k:int):
        seen = {}
        left, maxfreq, maxres = 0,0,0
        for right, _ in enumerate(s):
            seen[s[right]] = 1+ seen.get(s[right], 0)
            maxfreq = max(maxfreq, seen[s[right]])
            if (right-left+1) - maxfreq > k:
                seen[s[left]] -= 1
                left+=1
            maxres = max(maxres, right-left+1)
        return maxres


sol = Solution()
print(sol.characterReplacement("AABABBA", 1))