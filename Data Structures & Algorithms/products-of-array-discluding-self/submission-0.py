class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix, suffix = [0] * len(nums), [0] * len(nums)

        for i in range(len(nums)):
            j = len(nums) - 1 - i
            # get prefix and suffix
            if i > 0:
                prefix[i] = prefix[i - 1] * nums[i-1]
                suffix[j] = suffix[j + 1] * nums[j+1]
            else: 
                prefix[i] = 1
                suffix[j] = 1

        result = [] 
        for i in range(len(suffix)):
            result.append(suffix[i] * prefix[i])
        
        return result