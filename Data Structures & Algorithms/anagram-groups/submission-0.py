class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        match = dict()
        
        for i in range(len(strs)):
            sorted_str = str(sorted(strs[i]))

            if sorted_str in match:
                match[sorted_str].append(strs[i])
            else:
                match[sorted_str] = [strs[i]]
        

        for j in match:

            result.append(match[j])

        return result


            

