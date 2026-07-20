from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        final_arr = []
        counts = Counter(arr1)
        for i in arr2:
            final_arr.extend([i] * counts[i])
            for _ in range(counts[i]):
                arr1.remove(i)
        return final_arr + sorted(arr1)
        