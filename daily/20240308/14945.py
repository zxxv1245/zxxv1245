N = int(input())

dp = [[0]*N for _ in range(N)]

for i in range(0,N) :
    dp[0][i] = i+1
    dp[i][0] = 1

for i in range(1,N) :
    for j in range(1,N) :
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

ret =  dp[N-2][N-1]%10007
print(ret)
