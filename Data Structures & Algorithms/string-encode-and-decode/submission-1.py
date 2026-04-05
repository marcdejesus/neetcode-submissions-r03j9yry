class Solution:

    def encode(self, strs: List[str]) -> str:
        result = "" 
        for s in strs:
            result += "67" + s[::-1]
        return result

    def decode(self, s: str) -> List[str]:
        if len(s) <= 0:
            return []

        result = s[2:].split("67")
        for i, r in enumerate(result):
            result[i] = r[::-1]
        return result