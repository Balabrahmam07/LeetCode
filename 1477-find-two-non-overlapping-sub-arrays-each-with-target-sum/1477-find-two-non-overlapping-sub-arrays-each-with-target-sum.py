class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        left = 0


        current_sum = 0

        best = [float("inf")] * len(arr)

        answer = float("inf")

        for right in range(len(arr)):

            current_sum += arr[right]

            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:

                length = right - left + 1

                if left > 0:
                    answer = min(answer, length + best[left - 1])

                best[right] = min(best[right], length)

            if right > 0:
                best[right] = min(best[right], best[right - 1])
        return -1 if answer == float('inf') else answer