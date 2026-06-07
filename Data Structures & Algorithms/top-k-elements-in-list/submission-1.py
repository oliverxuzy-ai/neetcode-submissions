import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()

        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1
        

        heap =[]

        for num, freq in freq_map.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        

        result = []
        for freq, num in heap:
            result.append(num)
        
        return result





        


        