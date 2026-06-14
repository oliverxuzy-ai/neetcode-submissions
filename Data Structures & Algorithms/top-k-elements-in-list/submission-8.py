import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [,1,]
        freq = defaultdict(int)

        result = []

        for n in nums:
            freq[n] += 1


        bucket = [[] for _ in range(len(nums)+1)]
        
        
        for i in freq:
            bucket[freq[i]].append(i)
        
        for j in range(len(bucket)-1, -1, -1):
            for n in bucket[j]:
                if bucket[j] is not None and k > 0:
                    result.append(n)
                    k -= 1

        

        return result



        









        


        