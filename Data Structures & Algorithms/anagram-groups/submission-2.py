class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for elem in strs:
            key = tuple(sorted(elem))
            if key not in hm:
                hm[key] = []
            hm[key].append(elem)
        return list(hm.values())