class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()

        # [4,5,6] -> [6,5,4]:[0,1,2]

        for i in range(len(nums)):
            diff[target - nums[i]] = i

        
        for j in range(len(nums)):
            if nums[j] in diff and j != diff[nums[j]]:
                return [j,diff[nums[j]]]

