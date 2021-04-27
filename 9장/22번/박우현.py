class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        t=[]
        stack=[]
        
        for i in range(len(T)):
            if len(stack)>0:
                while len(stack)>0 and T[stack[len(stack)-1]]<T[i]:
                    index=stack.pop()
                    t[index]=i-index
            t.append(0)
            stack.append(i)
            
        return t
