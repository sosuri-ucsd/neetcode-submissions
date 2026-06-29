class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        count = {}
        for char in s1:
            count[char] = count.get(char, 0) + 1
        for char in s2:
            count[char] = count.get(char, 0) - 1
        return all(v == 0 for v in count.values())