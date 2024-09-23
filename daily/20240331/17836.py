from collections import deque

def bfs() :

    visited = [[[0]*M for _ in range(N)]for _ in range(2)]
    Q = deque()
    Q.append((0,0,0))
    visited[0][0][0] = 1

    while Q :
        k,x,y = Q.popleft()
        if x == N-1 and y == M-1 :
            return visited[k][x][y]-1
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            if 0<=nx<N and 0<=ny<M :
                if k == 0 :
                    if lst[nx][ny] == 0 and visited[k][nx][ny] == 0 :
                        visited[k][nx][ny] = visited[k][x][y] + 1
                        Q.append((k,nx,ny))
                    elif lst[nx][ny] == 2 and visited[k][nx][ny] == 0 :
                        visited[k+1][nx][ny] = visited[k][x][y] + 1
                        Q.append((k+1,nx,ny))
                else :
                    if visited[k][nx][ny] == 0 :
                        visited[k][nx][ny] = visited[k][x][y] + 1
                        Q.append((k,nx,ny))
    return -1
N,M,T = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]


ret = bfs()
if ret == -1 :
    print('Fail')
else :
    if ret > T :
        print('Fail')
    else :
        print(ret)