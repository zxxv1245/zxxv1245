
def dfs(i,j,k) :
    global cnt

    if i >= N or j >= N or i < 0 or j < 0 :
        return
    if lst[i][j] == 1 :
        return
    if i == N-1 and j == N-1 :
        cnt +=1
        return

    prex,prey = i,j
    if k == 1 :
        dfs(i,j+1,1)
        if j+1<N and lst[i][j+1] != 1 :
            dfs(i+1,j+1,2)
    elif k == 2 :
        if i+1 < N and j+1 < N and lst[i+1][j+1] != 1 :
            dfs(i,j+1,1)
            dfs(i + 1, j, 3)
        dfs(i+1,j+1,2)

    elif k == 3 :
        if i+1 < N and lst[i+1][j] != 1 :
            dfs(i+1,j+1,2)
        dfs(i+1,j,3)

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
cnt = 0
dfs(0,1,1)
print(cnt)
