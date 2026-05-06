class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        i = 0 
        j = 0 

        min_len = float('inf') 
        max_sum = 0
        
        while j < len(nums):
            max_sum += nums[j]

            if max_sum < k:
                j += 1
            elif max_sum >= k:
                min_len = min(min_len, (j - i + 1))

                while max_sum >= k:
                    min_len = min(min_len, (j - i + 1))
                    max_sum -= nums[i]
                    i += 1

                j += 1

        return 0 if min_len == float('inf') else min_len 