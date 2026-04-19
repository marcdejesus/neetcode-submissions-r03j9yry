class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums) - 2):

            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:

                sum_triplet = nums[i] + nums[left] + nums[right]

                if sum_triplet < 0:
                    left += 1
                elif sum_triplet > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    right -= 1
            
        return res