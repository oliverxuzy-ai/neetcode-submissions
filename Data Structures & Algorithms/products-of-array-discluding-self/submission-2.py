class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = []


        for i in range(len(nums)):
            if i != 0:
                prefix[i] = prefix[i-1] * nums[i -1]

                suffix[len(nums) - i - 1] = suffix[len(nums) - i] * nums[len(nums) - i]
            else:
                prefix[i] = 1
                suffix[i] = 1
        
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result
