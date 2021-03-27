def score(self,result:str):
    final_score = 0
    scores=0
    for i in result:
        if i == 'O':
            scores += 1
        elif i == 'X':
            final_score += scores
            scores = 0 
        else:
            pass
        
   if 'X' in result :
       return final_score
   else:
       return scores
