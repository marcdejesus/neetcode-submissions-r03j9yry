class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        left, right = 0, 0
        seen = set()
        
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                res = max(res, right - left)
            else: 
                seen = set()
                left += 1
                right = left

        return res
