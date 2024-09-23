N, L = map(int,input().split()) # N 신호등 갯수 L 도로 길이
lst = []
copy_lst = []
for _ in range(N) :
    D,R,G = map(int,input().split()) # D 신호등 위치 R 적색신호 길이 G 녹색신호 길이
    lst.append([D,0,R])
    copy_lst.append([D,R,G])

time = 0 # 시간
S = 0
arr = [0]*(L+1)
for i in lst:
    arr[i[0]] = 1
while S < L :
    time += 1

    for j in range(N) :
        if arr[lst[j][0]] == 1 :
            if time == lst[j][2] :
                arr[lst[j][0]] = 0
                lst[j][1] += copy_lst[j][1]+copy_lst[j][2]
                lst[j][2] += copy_lst[j][2] + copy_lst[j][1]
        elif arr[lst[j][0]] == 0 :
            if time == lst[j][1] :
                arr[lst[j][0]] = 1

    if arr[S + 1] == 0 :
        S += 1

print(time)