list = [1, 4, 3, 2]
s_list = sorted(list) # 정렬 
#s_list = [1,2,3,4]
#pair로 나누면 어차피 2개씩 나눠지는데 
#두 페어에서 작은수 덧셈이 제일 큰 수이려면 [1,2],[3,4]가 되니까
print(s_list[0] + s_list[2])
