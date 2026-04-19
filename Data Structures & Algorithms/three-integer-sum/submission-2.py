class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Sort nums array
        nums.sort()
        
        # Init result array
        res = []

        # Loop to check for triplets
        for i in range(len(nums) - 2):

            # End early if smallest number is positive (no combinations can = 0)
            if nums[i] > 0:
                break

            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Declare left and right
            if i > len(nums) - 3:
                break
            left = i + 1
            right = len(nums) - 1

            # Use sliding window to find valid triplet
            while left < right:
                
                # Triplet validation logic
                sum_triplet = nums[i] + nums[left] + nums[right]
                if sum_triplet > 0:
                    right -= 1
                elif sum_triplet < 0:
                    left += 1
                else:
                    # Add result
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1

                    # Skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    right -= 1
        return res


                



