class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p, max_p=prices[0], prices[0]
        profit=[0]
        for price in prices[1:]:
            if min_p>price:
                min_p=price
                max_p=min_p
                continue
            if max_p<=price: max_p=price
            profit.append(max_p-min_p)
        return max(profit)
