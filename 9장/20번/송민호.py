
def correct_char(self, s: str):
  stack=[] 
  //딕셔너리 만들기(키:값)//  
  table= {  
    ')' : '(' ,
    ']' : '[' ,
    '}' : '{'
  }
  // 키값과 마지막 문자 비교// 
  for char in s:
    if char not in table:
      stack.append(char)
    elif table[char] != stack.pop():
      return False
    
  return 0
