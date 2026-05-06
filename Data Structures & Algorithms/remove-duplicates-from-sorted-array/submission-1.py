class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 
        r = 1 
        temp = 1

        nums[0] = nums[l]

        while r < len(nums):
            while r < len(nums) and nums[l] == nums[r]:
                r += 1

            if r < len(nums):

                l = r
                nums[temp] = nums[r]
                temp += 1
                r += 1
                
        return temp

                
