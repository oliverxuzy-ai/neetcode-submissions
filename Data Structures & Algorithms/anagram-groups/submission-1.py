class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        match = dict()
        
        for i in range(len(strs)):

            sorted_str = [0] * 26
            for s in strs[i]:
                idx = ord(s) - ord('a')
                sorted_str[idx] += 1

            # sorted_str = str(sorted(strs[i]))
            sorted_str = tuple(sorted_str)
            if sorted_str in match:
                match[sorted_str].append(strs[i])
            else:
                match[sorted_str] = [strs[i]]
        

        for j in match:

            result.append(match[j])

        return result


            

