class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}
        for elem in s:
            if elem not in hm1:
                hm1[elem] = 1
            else:
                hm1[elem] += 1
        for elem in t:
            if elem not in hm2:
                hm2[elem] = 1
            else:
                hm2[elem] += 1
        return hm1 == hm2