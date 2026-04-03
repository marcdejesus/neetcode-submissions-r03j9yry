class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        differences = {}
        
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in differences:
                return [differences[difference], i]

            differences[nums[i]] = i