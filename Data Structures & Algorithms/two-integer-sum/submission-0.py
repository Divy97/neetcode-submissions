class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum_map = {}
        for index,value in enumerate(nums):
            complement = target - value
            if complement in twoSum_map:
                return [twoSum_map[complement],index]
            twoSum_map[value] = index
        return []