dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(i,j) :
    global maxV
    visited= [[0]*M for _ in range(N)]
    visited[i][j] = 1
    while Q :
        x,y = Q.popleft()

        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<= nx < N and 0<=ny<M and lst[nx][ny] == 'L' and visited[nx][ny] == 0 :
                visited[nx][ny] = visited[x][y] + 1
                Q.append((nx,ny))

    for x in range(N) :
        for y in range(M) :
            if visited[x][y] >= 1 :
               maxV = max(maxV,visited[x][y])


from collections import deque

N,M = map(int,input().split())

lst = [list(input()) for _ in range(N)]
Q = deque()

maxV = -21e8
for i in range(N) :
    for j in range(M) :
        if lst[i][j] == 'L' :
            Q.append((i,j))
            bfs(i,j)

print(maxV-1)