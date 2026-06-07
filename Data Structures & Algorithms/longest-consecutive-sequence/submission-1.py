class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_num = 1
        temp_max = 1

        if nums == []:
            return 0

        for i in range(len(nums)):
            temp = nums[i]

            while temp+1 in nums:
                temp_max += 1
                temp += 1
            
            max_num = max(max_num, temp_max)
            temp_max = 1
            
            
            
        return max_num