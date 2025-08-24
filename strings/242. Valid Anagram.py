class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        s1 = [0 for i in range(26)]
        t1 = [0 for i in range(26)]
        for i in range(len(s)):
            sid = ord(s[i]) - ord('a')
            tid = ord(t[i]) - ord('a')
            s1[sid] = 1+ s1[sid]
            t1[tid] = 1+ t1[tid]
        s1 = "".join([str(c) for c in s1])
        t1 = "".join([str(c) for c in t1])
        if s1 == t1: return True
        return False
    

sol = Solution()
print(sol.isAnagram('anagram', 'nagaram'))