class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, j in enumerate(nums):
            remaining = target - j
            if remaining in hm:
                return [hm[remaining], i]
            hm[j] = i
        return [-1, -1]

        