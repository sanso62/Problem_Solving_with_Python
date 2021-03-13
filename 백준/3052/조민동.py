nums=[int(input()) for _ in range(10)]
set_nums=set([i%42 for i in nums])
print(len(set_nums))
