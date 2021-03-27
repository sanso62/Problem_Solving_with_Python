test_case=int(input())

for t in range(test_case):
	score=0
	correct_count=0
	result=input()

	for index in range(len(result)):
		if result[index]=='O':
			correct_count+=1
			score+=correct_count
		else:
			correct_count=0

	print(score)
