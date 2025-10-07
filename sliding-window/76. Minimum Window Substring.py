class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count, window = {}, {}
        have, need = 0, len(t)

        for ch in t:
            count[ch] = 1 + count.get(ch, 0)
        need = len(count)
        res, reslen = [-1, -1], float("inf")
        left, right = 0, 0
        while right < len(s):
            char = s[right]
            window[char] = 1 + window.get(char, 0)
            if char in count and window[char] == count[char]:
                have += 1
            while have == need:
                if reslen > right - left + 1:
                    reslen = right - left + 1
                    res = [left, right]
                window[s[left]] -= 1
                if s[left] in count and window[s[left]] < count[s[left]]:
                    have -= 1
                left += 1
            right += 1
        l, r = res
        return s[l : r + 1] if reslen != float("inf") else ""


sol = Solution()
print(sol.minWindow("OUZODYXAZV", "XYZ"))
print(sol.minWindow("bbaa", "aba"))
