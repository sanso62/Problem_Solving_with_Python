stack=[]

def push(self, x:):
  stack.append(x)
  for _ in range(len(stack)-1):
    stack.append(stack.popleft())
    
def pop(self):
  return stack.popleft()

def top(self):
  return stack[0]

def empty(self):
  return len(stack) == 0 
    
    
    
    
