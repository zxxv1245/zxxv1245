dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs(x,y) :

    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1

    while Q :
        x,y = Q.popleft()
        if lst[x][y] == 1:
            return visited[x][y] - 1

        for a in range(8) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                Q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1



from collections import deque

T = int(input())

for Test in range(1,T+1) :
    N = int(input())

    lst = [[0]*N for _ in range(N)]
    Q = deque()
    sx,sy = map(int,input().split())
    fx,fy = map(int,input().split())
    lst[fx][fy] = 1
    Q.append((sx,sy))

    print(bfs(sx,sy))