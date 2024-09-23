N, K = map(int,input().split())
cnt = 0
student = {}
for i in range(2) :
    for j in range(1,7) :
        student[(i,j)] = 0


for a in range(N) :
    sex, grabe = map(int,input().split())
    student[(sex, grabe)] += 1

for b in student :
    if 0 < student[b] <= K :
        cnt += 1
    elif student[b] == 0 :
        pass
    else :
        if student[b] % K != 0:
            cnt += student[b] // K + 1
        else :
            cnt += student[b]// K
print(cnt)