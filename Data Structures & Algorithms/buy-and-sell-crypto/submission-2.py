class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_pro = 0



        for r in range(1,len(prices)):
            if prices[r] - prices[l] > 0:
                max_pro = max(max_pro, prices[r] - prices[l])
            else:
                l = r




        
        return max_pro




