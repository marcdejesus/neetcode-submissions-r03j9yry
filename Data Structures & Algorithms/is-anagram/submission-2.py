class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Skip when string lengths aren't equal
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
