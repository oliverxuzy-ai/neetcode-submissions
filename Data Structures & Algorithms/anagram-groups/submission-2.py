class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        match = defaultdict(list)

        for s in strs:
            # transform
            count_key = [0] * 26
            for j in s:
                idx = ord(j) - ord('a')
                count_key[idx] += 1
                
            match[tuple(count_key)].append(s)

            # if tuple(count_key) in match:
            #     match[tuple(count_key)].append(i)
            # else:
            #     match[tuple(count_key)].append(i)
        

        # for j in match:
        #     result.append(match[i])

        return list(match.values())
            

        
        



            

