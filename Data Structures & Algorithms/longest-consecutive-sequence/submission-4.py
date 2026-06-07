class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_num = 1
        temp_max = 1
        i = 0

        if nums == []:
            return 0

        while i <= len(nums) - 1:
            temp = nums[i]

            if nums[i] - 1 in set(nums):
                i += 1
                continue

            while temp+1 in set(nums):
                temp_max += 1
                temp += 1
            
            max_num = max(max_num, temp_max)
            temp_max = 1
            i += 1
            
            
            
        return max_num


        # if num
        # 2, 


        # dict[max_number] = length
