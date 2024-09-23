from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(i,j) :
    global N
    global M
    visited = [[0]*(M+1) for _ in range(N+1)]
    Q = deque()
    visited[i][j] = 1
    lst[i][j] = 0
    Q.append([i,j])

    while Q :
        x,y = Q.popleft()

        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<= nx < N and 0<=ny<M and lst[nx][ny] == 1 and visited[nx][ny] == 0 :
                Q.append([nx,ny])
                visited[nx][ny] = 1
                lst[nx][ny] = 0

T = int(input())

for Test in range(1,T+1) :
    M,N,K = map(int,input().split())
    lst = [[0]*M for _ in range(N)]
    for _ in range(K) :
        y,x = map(int,input().split())
        lst[x][y] = 1

    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if lst[i][j] == 1 :
                bfs(i,j)
                cnt += 1

    print(cnt)