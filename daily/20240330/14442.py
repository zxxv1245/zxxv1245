from collections import deque

def bfs() :

    visited = [[[0]*M for _ in range(N)] for _ in range(K+1)]
    visited[K][0][0] = 1
    Q = deque()
    Q.append((K,0,0))

    while Q :
        k,x,y = Q.popleft()
        if x == N-1 and y == M-1 :
            return visited[k][x][y]
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            if 0 <= nx < N and 0 <= ny < M :
                if not lst[nx][ny] and not visited[k][nx][ny]:
                    visited[k][nx][ny] = visited[k][x][y] + 1
                    Q.append((k,nx,ny))
                elif lst[nx][ny] and k>0 and not visited[k-1][nx][ny]:
                    visited[k-1][nx][ny] = visited[k][x][y] + 1
                    Q.append((k-1,nx,ny))

    return -1

N,M,K = map(int,input().split())

lst = [list(map(int,input())) for _ in range(N)]

print(bfs())