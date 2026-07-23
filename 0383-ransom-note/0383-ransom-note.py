class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = Counter(ransomNote)
        x = Counter(magazine)
        for i in s:
            if x[i] < s[i]:
                return False
        return True