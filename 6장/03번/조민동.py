class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = [log for log in logs if not log[-1].isdigit()]
        digits = [log for log in logs if log[-1].isdigit()]
        letters.sort(key = lambda x: x.split()[0])
        letters.sort(key = lambda x: x.split()[1:])
        
        return letters+digits
      
