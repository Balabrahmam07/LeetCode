class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        
        seen = set()
        max_window_sum = 0
        current_window_sum = 0
        left = 0

        for right in range(len(nums)):
            
            while nums[right] in seen :
                    current_window_sum -= nums[left]
                    seen.remove(nums[left])
                    left += 1
                    
            current_window_sum += nums[right]
            seen.add(nums[right])

            if right - left + 1 == k:
                max_window_sum = max(max_window_sum, current_window_sum)
                current_window_sum -= nums[left]
                seen.remove(nums[left])
                left += 1

        return max_window_sum
        