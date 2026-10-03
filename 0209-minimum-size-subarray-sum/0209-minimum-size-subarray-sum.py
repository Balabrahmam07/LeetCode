class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len_window = float('inf')
        sum_elements = 0
        left = 0
        for right in range(len(nums)):

            sum_elements += nums[right]

            while sum_elements >= target:
                min_len_window = min(min_len_window, right - left + 1)
                sum_elements -= nums[left]
                left += 1
        return min_len_window if min_len_window != float('inf') else 0