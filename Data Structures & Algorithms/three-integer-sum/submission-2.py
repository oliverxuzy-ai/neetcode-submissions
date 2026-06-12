class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        result = []

        while i < len(nums) - 2:
            pair = -nums[i]

            if i >0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] < pair:
                    l += 1
                
                elif nums[l] + nums[r] > pair:
                    r -= 1

                else:
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
            
            i += 1
        
        return result









