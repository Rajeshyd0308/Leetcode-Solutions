class Solution(object):
    # def count(self, amount, coins):
    #     if amount==0:
    #         return 1
    #     elif amount<0:
    #         return 0
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        vals = [0]*(amount+1)
        vals[0] = 1

        for c in coins:
            for i in range(c, amount+1):
                vals[i] = vals[i] + (vals[i-c])
        return vals[amount]
