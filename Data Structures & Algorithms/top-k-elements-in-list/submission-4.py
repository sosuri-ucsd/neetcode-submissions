class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        
        for elem in nums:
            if elem not in hm:
                hm[elem] = 1
            else:
                hm[elem] += 1

        for num, cnt in hm.items():
            bucket[cnt].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for elem in bucket[i]:
                res.append(elem)
                if len(res) == k:
                    return res

        
                
                