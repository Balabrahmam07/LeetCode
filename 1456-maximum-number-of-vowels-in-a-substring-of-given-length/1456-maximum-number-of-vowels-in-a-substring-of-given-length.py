class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        count = 0

        for i in range(k):
            count += s[i] in vowels
        
        max_count = count

        for right in range(k, len(s)):

            count += s[right] in vowels
            
            left = right - k

            count -= s[left] in vowels
            
            max_count = max(max_count, count)
            
        return max_count


         