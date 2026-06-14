class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        pairs = defaultdict(list)


        for s in strs:
            sorted_str = "".join(sorted(s))

            pairs[sorted_str].append(s)

        
        for i in pairs:
            result.append(pairs[i])
        
        return result

            

        
        



            

