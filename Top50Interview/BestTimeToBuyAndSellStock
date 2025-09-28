class Solution(object):
    def maxProfit(self, prices):
        p = prices
        sum = 0
        l = len(p)
        for i in range(0, l-1):
            if (p[i+1] - p[i]) > 0:
                sum += (p[i+1] - p[i])
        return sum
        
