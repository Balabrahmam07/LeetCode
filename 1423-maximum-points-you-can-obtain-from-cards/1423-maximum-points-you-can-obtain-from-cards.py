class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k

        if window_size == 0:
            return sum(cardPoints)

        current_window_sum = sum(cardPoints[:window_size])
        min_window_sum = current_window_sum
        total_window_sum = current_window_sum

        left = 0
        for right in range(window_size ,n):
            
            current_window_sum += cardPoints[right] - cardPoints[left]

            total_window_sum += cardPoints[right]

            min_window_sum = min(min_window_sum, current_window_sum)
            
            left += 1
        
        return total_window_sum - min_window_sum





        

        