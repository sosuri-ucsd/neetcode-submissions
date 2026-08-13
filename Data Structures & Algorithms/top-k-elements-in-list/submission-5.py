class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])
        
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
            
        for num, cnt in hm.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
