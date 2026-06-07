class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()
        result = []

        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1

        j = 0
        while j < k:
            top = max(freq_map, key=freq_map.get)
            result.append(top)

            freq_map.pop(top)

            j += 1

        return result




        


        