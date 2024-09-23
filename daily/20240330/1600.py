from collections import deque
import sys
input = sys.stdin.readline
def bfs() :

    visited = [[[0]*M for _ in range(N)] for _ in range(K+1)]
    visited[K][0][0] = 1
    Q = deque()
    Q.append((K,0,0))

    while Q :
        k,x,y = Q.popleft()
        if x== N-1 and y == M-1 :
            return visited[k][x][y]-1
        if k > 0 :
            for a in range(4,12) :
                nx = x+dx[a]
                ny = y+dy[a]
                if 0<=nx<N and 0<=ny<M :
                    if not lst[nx][ny] and not visited[k-1][nx][ny] :
                        visited[k-1][nx][ny] = visited[k][x][y] + 1
                        Q.append((k-1,nx,ny))
        for a in range(4) :
            nx = x+dx[a]
            ny = y+dy[a]
            if 0<=nx<N and 0<=ny<M :
                if not lst[nx][ny] and not visited[k][nx][ny] :
                    visited[k][nx][ny] = visited[k][x][y] + 1
                    Q.append((k,nx,ny))

    return -1
K = int(input())
M,N = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]

dx = (0,1,0,-1,-2,-1,1,2,2,1,-1,-2)
dy = (1,0,-1,0,1,2,2,1,-1,-2,-2,-1)

print(bfs())