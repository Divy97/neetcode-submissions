class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0 
        j = 0 

        max_value = deque()
        result = []
        while j < len(nums):

            while max_value and nums[max_value[-1]] < nums[j]:
                max_value.pop()

            max_value.append(j)

            if (j - i + 1) < k:
                j += 1
            elif (j - i + 1) == k:
                result.append(nums[max_value[0]])
                if max_value[0] == i:
                    max_value.popleft()
                i += 1
                j += 1

        return result