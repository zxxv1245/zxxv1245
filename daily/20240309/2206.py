from collections import deque

def bfs(x,y,v) :
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    Q = deque()
    Q.append((x, y, v))
    visited[x][y][0] = 1

    while Q :
        x,y,v = Q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][0]
        for a in range(4) :
            nx = x+dx[a]
            ny = y+dy[a]
            if 0<=nx<N and 0<=ny<M :
                if lst[nx][ny] == 0 and visited[nx][ny][0] == 0 :
                    Q.append((nx,ny,v))
                    visited[nx][ny][0] = visited[x][y][0] +1
                    visited[nx][ny][1] = v
                elif lst[nx][ny] == 1 and visited[nx][ny][0] == 0 and v == 0 :
                    Q.append((nx,ny,1))
                    visited[nx][ny][0] = visited[x][y][0] + 1
                    visited[nx][ny][1] = 1
                elif lst[nx][ny] == 0 and visited[nx][ny][0] != 0 and visited[nx][ny][1] == 1 and v==0:
                    Q.append((nx,ny,0))
                    visited[nx][ny][0] = visited[x][y][0] + 1
                    visited[nx][ny][1] = 0
    return -1



N,M = map(int,input().split())
lst = [list(map(int,input())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

print(bfs(0,0,0))