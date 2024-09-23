import sys
input = sys.stdin.readline
def check(i,j) :
    ret = True
    for di,dj in [(0,1),(1,1),(1,0)] :
        ni,nj = i+di,j+dj
        if ni<N and nj<N and lst[ni][nj] == 0 : continue
        else :
            ret = False
            break
    return ret
def dfs(x,y,pre) :

    if x == N-1 and y == N-1 :
        return 1

    if dp[x][y] == -1 :
        dp[x][y] = 0
        if pre == 1 :
            if y+1<N and lst[x][y+1] == 0 :
                dp[x][y] += dfs(x,y+1,1)
            if check(x ,y) :
                dp[x][y] += dfs(x+1,y+1,2)
        elif pre == 2 :
            if y+1<N and lst[x][y+1] == 0 :
                dp[x][y] +=dfs(x,y+1,1)
            if check(x , y):
                dp[x][y] +=dfs(x+1,y+1,2)
            if x+1<N and lst[x+1][y] == 0 :
                dp[x][y] +=dfs(x+1,y,3)
        elif pre == 3 :
            if check(x , y):
                dp[x][y] +=dfs(x+1,y+1,2)
            if x+1<N and lst[x+1][y] == 0 :
                dp[x][y] +=dfs(x+1,y,3)
    return dp[x][y]


N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]

dp = [[-1]*N for _ in range(N)]
dfs(0,1,1)
for i in dp :
    print(*i)
print(dp[0][1])
