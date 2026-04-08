class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        result = 0 # Max length
        
        for i, num in enumerate(nums):
            # Check for sequence start
            if num - 1 not in numset: 
                seq_len = 1
                curr = num
                # Determine sequence length
                while curr + 1 in numset: 
                    seq_len += 1
                    curr += 1
                result = max(result, seq_len)


        return result


                