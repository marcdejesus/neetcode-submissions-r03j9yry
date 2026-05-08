class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        l = 0
        curr = float("-inf")

        for r in range(len(nums)):
            curr = max(curr, nums[r])

            if r-l+1 == k:
                res.append(curr)

                if nums[l] == curr:
                    curr = float("-inf")
                    temp = l + 1
                    while temp <= r:
                        curr = max(curr, nums[temp])
                        temp+= 1
                l+= 1
        
        return res
