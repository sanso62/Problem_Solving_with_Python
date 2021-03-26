def watertrap(self, height:List[int]):
  left_max=[]
  right_max=[]
  volume =0 
  for left in range(len(height)):
    left_max.append(max(height[0:left])
  for right in range(len(height)):
    right_max.append(max(height[right:int(len(height))-1]                    
  for i in range(len(height)):
     if left_max[i] <= right_max[i]:
                         volume += left_max[i]-height[i]
     else:
                         volume += right_max[i]-height[i]
  return volume                       
