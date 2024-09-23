N = int(input())

DP = [0]*(N+1)

lst = [list(map(int,input().split())) for _ in range(N)]

for i in range(N-1,-1,-1) :
    if i+lst[i][0] <= N :
        DP[i] = max(DP[i+lst[i][0]]+lst[i][1],DP[i+1])
    else :
        DP[i] = DP[i+1]

print(DP[0])
