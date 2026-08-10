class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for elem in nums:
            if elem in hm:
                return True
            hm[elem] = 1
        return False
        
