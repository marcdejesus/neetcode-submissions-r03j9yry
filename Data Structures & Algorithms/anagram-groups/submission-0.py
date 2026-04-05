class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group_map = defaultdict(list)

        # ASCII for 'a' starts at 97
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c)-97] += 1
            group_map[tuple(counts)].append(s)

        return list(group_map.values())