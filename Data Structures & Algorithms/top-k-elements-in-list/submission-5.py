import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()

        
        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1


        result = []
        heapq.heapify(result)

        for j in freq_map:
            heapq.heappush(result,(freq_map[j], j))

            if len(result) > k:
                heapq.heappop(result)
        
        return [i[1] for i in result]








        


        