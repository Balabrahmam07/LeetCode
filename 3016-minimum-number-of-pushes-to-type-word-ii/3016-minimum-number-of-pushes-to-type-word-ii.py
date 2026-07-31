from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        word = Counter(word)
        count = 0
        alpha_list = [[] for _ in range(8)]
        for i, (wrd, freq) in enumerate(word.most_common()):
            idx = i % 8
            if len(alpha_list[idx]) < 8:
                alpha_list[idx].append(wrd)
                count += (alpha_list[idx].index(wrd) + 1) * freq
        return count