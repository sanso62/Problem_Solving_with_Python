class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        for idx,t in enumerate(T):
            cnt = 0
            for other_t in T[idx+1:]:
                cnt+=1
                if other_t > t:
                    T[idx] = cnt
                    break
            else:
                T[idx] = 0
        return T      
 
