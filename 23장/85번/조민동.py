class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        else: 
            stack=[0,1]
            for i in range(n-1):
                if i==n-2:
                    return stack.pop()+stack.pop()
                pre=stack.pop()
                last=pre+stack.pop()
                stack.append(pre)
                stack.append(last)
