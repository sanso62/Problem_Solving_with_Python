def maxProfit(self, prices: List[int]) -> int:
	minprice=1000000000
	profit=0

	for i in range(len(prices)):
		if minprice>prices[i]:
			minprice=prices[i]
		if prices[i]-minprice>profit:
			profit=prices[i]-minprice

	return profit
