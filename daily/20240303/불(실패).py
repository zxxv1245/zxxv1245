dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs() :
    F = [0,0,0,0]
    while Q :
        x,y = Q.popleft()
        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                if lst[x][y] == 'F' :
                    if nx < 0 :
                        F[0] = 1
                    elif nx >= N :
                        F[2] = 1
                    elif ny < 0 :
                        F[3] = 1
                    elif ny >= M :
                        F[1] = 1
                elif lst[x][y] == 'J' :
                    if nx < 0:
                        return visited[x][y]
                    elif nx >= N and F[2] == 0 :
                        return visited[x][y]
                    elif ny < 0 :
                        return visited[x][y]
                    elif ny >= M and F[1] == 0 :
                        return visited[x][y]
                    else :
                        return 'IMPOSSIBLE'
            elif 0<=nx<N and 0<=ny<M and lst[nx][ny] == '.' and visited[nx][ny] == 0 :
                Q.append((nx,ny))
                lst[nx][ny] = lst[x][y]
                visited[nx][ny] = visited[x][y] + 1
            elif 0<=nx<N and 0<=ny<M and lst[x][y] == 'F' and lst[nx][ny] in [',','J']:
                Q.append((nx, ny))
                lst[nx][ny] = lst[x][y]
                visited[nx][ny] = visited[x][y] + 1

    return 'IMPOSSIBLE'

from collections import deque

N,M = map(int,input().split())

lst = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
Q = deque()
for i in range(N) :
    for j in range(M) :
        if lst[i][j] == 'J' :
            Q.append((i,j))
            visited[i][j] = 1
for i in range(N) :
    for j in range(M) :
        if lst[i][j] == 'F' :
            Q.append((i,j))
            visited[i][j] = 1
print(bfs())