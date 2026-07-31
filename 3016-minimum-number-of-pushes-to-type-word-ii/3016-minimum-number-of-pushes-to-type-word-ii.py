from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        count = 0

        for i, (_, f) in enumerate(freq.most_common()):
            count += (i // 8 + 1) * f

        return count