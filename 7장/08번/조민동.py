class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []: return 0
        sum_height=sum(height)
        height: Deque = collections.deque(height)
        n=1
        total=0
        max_ele = sorted(height)[-1]
        while n<=max_ele:
            if height[0]<n: height.popleft()
            if height[-1]<n: height.pop()
            if height[0]>=n and height[-1]>=n: total += len(height)
            else: continue
        return total-sum_height
