class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pal_string = []
        for char in s:
            if char.isalnum():
                pal_string.append(char)
        return  "".join(pal_string) == "".join(pal_string[::-1])

        "a man a plan a canal panama"
        "amanap lanac a nalp a nam a"
