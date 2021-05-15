class Solution:
	def fib(self, n: int) -> int:
		fibonacci=[0,1,1]

		for i in range(n):
			fibonacci[i%3]=fibonacci[(i+1)%3]+fibonacci[(i+2)%3]

		return fibonacci[n%3]
