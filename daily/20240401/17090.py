import sys
sys.setrecursionlimit(10 ** 8)

N,M = map(int,input().split())
lst = [list(input()) for _ in range(N)]
arr = ['R','D','L','U']
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dp = [[0]*M for _ in range(N)]

def dfs(x,y) :

    if x<0 or x>=N or y < 0 or y>=M :
        return 1
    if dp[x][y] == 1 :
        return 1
    if dp[x][y] == -1 :
        return -1
    dp[x][y] = -1
    a = arr.index(lst[x][y])
    dp[x][y] = dfs(x+dx[a],y+dy[a])

    return dp[x][y]

cnt = 0
for i in range(N) :
    for j in range(M) :
        if dp[i][j] == 0 :
            if dfs(i,j) == 1 :
                cnt += 1
        elif dp[i][j] == 1 :
            cnt += 1
print(cnt)