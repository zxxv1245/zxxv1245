from collections import deque

def bfs(ex,ey) :
    global flag,cnt,level,ret,sx,sy,ans

    visited = [[0]*N for _ in range(N)]
    visited[sx][sy] = 1
    Q = deque()
    Q.append((sx,sy))

    while Q :
        x,y = Q.popleft()
        if x == ex and y == ey :
            ans = visited[x][y] - 1
            return
        for a in range(4) :
            nx,ny = x+dx[a],y+dy[a]
            if 0<=nx<N and 0<=ny<N :
                if lst[nx][ny]<= level and visited[nx][ny] == 0 :
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx,ny))

N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

for r in range(N) :
    for c in range(N) :
        if lst[r][c] == 9 :
            sx,sy = r,c
            lst[r][c] = 0
flag = 1
cnt = 0
level = 2
ret = 0
while True :

    arr = []
    for i in range(N) :
        for j in range(N) :
            ans = 0
            if 1 <= lst[i][j] < level :
                bfs(i,j)
                if ans >= 1 :
                    arr.append((i,j,ans))
    if not arr :
        flag = 0
    if flag == 0 :
        break
    arr.sort(key = lambda x:x[1])
    arr.sort(key = lambda x:x[0])
    arr.sort(key = lambda x:x[2])
    sx,sy = arr[0][0],arr[0][1]
    ret += arr[0][2]
    lst[sx][sy] = 0
    cnt += 1
    if cnt == level :
        level += 1
        cnt = 0

print(ret)