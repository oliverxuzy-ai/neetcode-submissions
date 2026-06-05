class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        judge = dict()

        for i in s:
            if i not in judge:
                judge[i] = 1
            else:
                judge[i] += 1
        
        for j in t:
            if j in judge and judge[j] > 0:
                judge[j] -= 1
            else:
                return False
        
        if sum(judge.values()) == 0:
            return True
        else:
            return False