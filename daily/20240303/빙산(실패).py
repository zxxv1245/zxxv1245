def bfs(x,y) :
    global maxV
    global cnt
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1

    while Q :
        x,y = Q.popleft()
        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny<M and lst[nx][ny] != 0 and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                Q.append((nx,ny))


    for i in range(N) :
        for j in range(M) :
            if lst[i][j] != 0 :
                for b in range(4) :
                    ni = i +dx[b]
                    nj = j +dy[b]
                    if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 0:
                        if lst[i][j] != 0:
                            lst[i][j] -= 1


    for i in range(N) :
        for j in range(M) :
            maxV = max(maxV,visited[i][j])
            if maxV == 0 :
                cnt = 0

from collections import deque

N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]

maxV = 0
cnt = 0
Q = deque()
for i in range(N) :
    for j in range(M) :
        if lst[i][j] != 0 :
            Q.append((i,j))
            bfs(i,j)
            cnt += 1
            if maxV >= 2 :
                break
    if maxV >= 2 :
        break
print(cnt)