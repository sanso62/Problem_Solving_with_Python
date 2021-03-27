n_quiz=int(input())
quizzes=[]
for i in range(n_quiz):
    quiz=input()
    quizzes.append(quiz)

total_score=0
score=0
pre_score=1
n=0
for quiz in quizzes:
    total_score = 0
    score = 0
    pre_score = 1
    n+=1
    for i, ox in enumerate(quiz):
        if ox == "O":
            score+=pre_score
            pre_score+=1
            # print(n, ox)
        elif ox=="X":
            total_score+=score
            score=0
            pre_score=1
        if i==len(quiz)-1: total_score+=score
    print(total_score)
