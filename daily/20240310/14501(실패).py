#퇴사
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
i = 0
maxV = -21e8

while i < N :
    DP = [0]*N
    if i + lst[i][0] <= N :
        DP[i] = lst[i][1]
        j = i + lst[i][0]                   # j 반복 범위 다시 설정
                                            # i = 1 일떄 j = 2
                                            # i = 1 일때 j = 3 이런식으로 가야함
    while j < N :
        if j +lst[j][0] <= N :
            DP[j] = lst[j][1]
            j += lst[j][0]
        else :
            j+= 1
    if maxV < sum(DP) :
        maxV = sum(DP)
        maxDP = DP
    i += 1
print(maxDP)
print(maxV)
