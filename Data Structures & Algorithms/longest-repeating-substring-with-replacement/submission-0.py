class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = defaultdict(int)
        res=0
        left=0

        for right in range(len(s)):
            freq[s[right]] +=1
            if max(freq.values()) + k < right - left + 1:
                freq[s[left]] -= 1
                left += 1
            res=max(res, right-left+1)
        return res