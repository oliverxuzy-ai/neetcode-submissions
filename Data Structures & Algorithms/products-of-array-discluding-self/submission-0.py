class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []

        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]

            temp_prod = 1

            for j in temp:
                temp_prod = temp_prod * j
            
            result.append(temp_prod)

        return result