def bfsA(x,y) :
    v = lst[x][y]
    visited[x][y] = 1
    while Q :
        x,y = Q.popleft()

        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<= nx < N and 0 <= ny < N and lst[nx][ny] == v and visited[nx][ny] == 0 :
                Q.append((nx,ny))
                visited[nx][ny] = 1

def bfsB(x,y) :
    visited[x][y] = 1
    while Q :
        x,y = Q.popleft()

        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<= nx < N and 0 <= ny < N and lst[x][y] in ['R','G'] and visited[nx][ny] == 0 :
                if lst[nx][ny] in ['R','G'] :
                    Q.append((nx,ny))
                    visited[nx][ny] = 1
            elif 0<= nx < N and 0 <= ny < N and lst[x][y] == 'B' and visited[nx][ny] == 0 :
                if lst[nx][ny] == 'B' :
                    Q.append((nx, ny))
                    visited[nx][ny] = 1

from collections import deque

N = int(input())
lst = [list(input()) for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
Q = deque()
cntA = 0
visited = [[0]*N for _ in range(N)]
for x in range(N) :
    for y in range(N) :
        if lst[x][y] in ['R','G','B'] and visited[x][y] == 0:
            Q.append((x,y))
            bfsA(x,y)
            cntA += 1

Q = deque()
cntB = 0
visited = [[0]*N for _ in range(N)]
for x in range(N) :
    for y in range(N) :
        if lst[x][y] in ['R','G','B'] and visited[x][y] == 0:
            Q.append((x,y))
            bfsB(x,y)
            cntB += 1

print(cntA, cntB)
