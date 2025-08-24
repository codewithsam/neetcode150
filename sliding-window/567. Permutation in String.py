class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False

        c1 = [0 for _ in range(26)]
        c2 = [0 for _ in range(26)]
        l, r = 0,0

        for j, n in enumerate(s1):
            c1[ord(n)- ord('a')] +=1
            c2[ord(s2[j]) - ord('a')] +=1

        for i in range(len(s2) - len(s1)):
           if c1 == c2: return True

           if i+ len(s1) < len(s2):
                c2[ord(s2[i]) - ord('a')] -= 1
                c2[ord(s2[i + len(s1)]) - ord('a')] +=1
        return False



sol = Solution()

print(sol.checkInclusion("ab", "eidbaooo"))