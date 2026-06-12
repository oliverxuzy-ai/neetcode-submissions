class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()

        # [4,5,6] -> [6,5,4]:[0,1,2]
        # target = [current_index, pair_index]

        # pair[pair_num] = pair_index
        # pair_num = target - current_num
        # 
        uniq_nums = set(nums)

        for i in range(len(nums)):
            diff[nums[i]] = i
        
        for n in range(len(nums)):
            if (target - nums[n]) in diff and n != diff[target - nums[n]]:
                return [n,diff[target - nums[n]]] 



