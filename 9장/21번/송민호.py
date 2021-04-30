def find_overlap(self, s:char):
  stack=[]
  char_box=[]
  //stack에 문자넣기//
  for char in s :
    stack.append(char)
  // 스택안 문자개수가 1이 될때 까지 스택 첫번째 문자와 다른 문자들을 계속 비교후 같으면 비교대상 문자를 삭제함 //  
  while len(stack) != 1 :
    for i in range(len(stack)-1):
      if stack.pop(0) = stack.pop(len(stack)-i) :
        stack.pop(len(stack)-i)
      //비교과정이 끝나면 스택 첫번째 문자는 char_box 리스트에 넣음//  
      char_box.append(stack.pop(0))
  //만약 스택안 문자개수가 1이 되면 그 문자는 char_box 리스트에 넣음//    
  if len(stack) = 1 :
    char_box.append(stack.pop())
  //char_box리스트안 문자를 사전식 순서로 나열//  
  sort.char_box
  //리스트 안 문자를 문자열로 추출//
  result_chars="".join(char_box)
  return result_chars          
