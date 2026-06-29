class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, j in enumerate(nums):
            new = target - j
            if new in hm:
                return [hm[new], i]
            else:
                hm[j] = i


        return [-1, -1]

        