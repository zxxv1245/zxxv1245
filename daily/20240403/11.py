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
    global cnt
    if lst[N-1][N-1] == 1 :
        print(0)
        exit()
    if x == N-1 and y == N-1 :
        cnt+=1
        return

    if pre == 1 :
        if y+1<N and lst[x][y+1] == 0 : # 가로 벽이 있으면 탐색 X
            dfs(x,y+1,1)
        if check(x ,y) : # 대각선이면 3방향 체크
            dfs(x+1,y+1,2)
    elif pre == 2 :
        if y+1<N and lst[x][y+1] == 0 :
            dfs(x,y+1,1)
        if check(x , y):
            dfs(x+1,y+1,2)
        if x+1<N and lst[x+1][y] == 0 :
            dfs(x+1,y,3)
    elif pre == 3 :
        if check(x , y):
            dfs(x+1,y+1,2)
        if x+1<N and lst[x+1][y] == 0 :
            dfs(x+1,y,3)


N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
dfs(0,1,1)
print(cnt)