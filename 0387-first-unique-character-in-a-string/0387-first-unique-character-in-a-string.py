class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, ch in enumerate(s):
            if s.find(ch) == s.rfind(ch):
                return i
        return -1