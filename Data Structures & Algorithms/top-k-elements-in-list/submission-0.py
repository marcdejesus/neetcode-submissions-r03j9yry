class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)

        most_common = counts.most_common(k)

        result = []
        for val in most_common:
            result.append(val[0])

        return result