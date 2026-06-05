class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = dict()
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for j in dic:
            if dic[j] > 1:
                return True
        
        return False