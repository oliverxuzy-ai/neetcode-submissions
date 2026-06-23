class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = [0] * 26
        match = [0] * 26

        if len(s1) > len(s2):
            return False
        
        for i in s1:
            target[ord(i) - ord('a')] += 1
        
        for s in s2[0:len(s1)]:
            match[ord(s) - ord('a')] += 1
        
        if target == match:
                return True

        for j in range(len(s1),len(s2)):
            
            match[ord(s2[j]) - ord('a')] += 1
            match[ord(s2[j-len(s1)]) - ord('a')] -= 1

            if target == match:
                return True
        
        return False



        
        # 1. initiate first sliding window

        