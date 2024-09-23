i,j = map(int,input().split())

dp = [[0]*(i+1) for _ in range(i+1)]

dp[1][1] = 1

for x in range(2,i+1) :
    for y in range(1,x+1) :
        dp[x][y] = dp[x-1][y-1] +dp[x-1][y]

# for i in dp :
    # print(*i)
print(dp[i][j])