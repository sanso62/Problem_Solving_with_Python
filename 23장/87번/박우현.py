class Solution:
	def climbStairs(self, n: int) -> int:
		method=[0,1,2]

		for i in range(n):
			method[i%3]=method[(i+1)%3]+method[(i+2)%3]

		return method[n%3]
