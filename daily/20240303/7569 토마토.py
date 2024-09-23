from collections import deque

def bfs() :

    while Q :
        x,y = Q.popleft()

        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<= nx < H*N and 0+N*(x//N)<= nx < N+N*(x//N) and 0<=ny<M and lst[nx][ny] == 0 :
                lst[nx][ny] = lst[x][y] + 1
                Q.append((nx,ny))
        for b in range(4,6) :
            nx = x + dx[b]
            ny = y + dy[b]
            if 0 <= nx < H * N and lst[nx][ny] == 0:
                lst[nx][ny] = lst[x][y] + 1
                Q.append((nx, ny))
    maxV = 1
    for i in range(H * N):
        for j in range(M):
            if lst[i][j] == 0 :
                return -1
            else :
                if maxV < lst[i][j] :
                    maxV = lst[i][j]
    return maxV-1

from collections import deque

M,N,H = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(H*N)]

dx = [0,1,0,-1,N,-N]
dy = [1,0,-1,0,0,0]
Q = deque()
for x in range(H*N) :
    for y in range(M) :
        if lst[x][y] == 1 :
            Q.append((x,y))


print(bfs())

