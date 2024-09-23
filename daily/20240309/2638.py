from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y) :
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1

    while Q :
        x,y = Q.popleft()

        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny<M :
                if lst[nx][ny] == 0 and visited[nx][ny] == 0 :
                    Q.append((nx,ny))
                    visited[nx][ny] = 1
                elif lst[nx][ny] == 1 :
                    visited[nx][ny] += 1

    for i in range(N) :
        for j in range(M) :
            if lst[i][j] == 1 and visited[i][j] >= 2 :
                lst[i][j] = 0

N,M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
Q = deque()

cnt = 0
for i in range(N) :
    for j in range(M) :
        if lst[i][j] == 0 :
            Q.append((i,j))
            bfs(i,j)
            cnt += 1
            ans = 0
            for x in range(N) :
                for y in range(M) :
                    if lst[x][y] == 1 :
                        ans += 1

            if ans == 0 :
                break
    if ans == 0 :
        break
print(cnt)