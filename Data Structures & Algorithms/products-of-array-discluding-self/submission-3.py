class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = []


        for i in range(len(nums)):
            if i != 0:
                prefix[i] = prefix[i - 1] * nums[i - 1]

                suffix[len(nums) - 1 - i] = suffix[len(nums) - i] * nums[len(nums) - i]

            
        return [(prefix[i] * suffix[i]) for i in range(len(nums))]
