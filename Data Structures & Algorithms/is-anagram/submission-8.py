class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}
        for i in s:
            if i not in hm1:
                hm1[i] = 1
            else:
                hm1[i] += 1
        for j in t:
            if j not in hm2:
                hm2[j] = 1
            else:
                hm2[j] += 1
        return hm1 == hm2