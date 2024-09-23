dx = [0,1,0,-1]
dy = [1,0,-1,0]

def maze(x,y) :
    global N
    global M
    Q = []
    visited = [[0]*M for _ in range(N)]

    Q.append([x,y])
    visited[x][y] = 1

    while Q :
        x, y = Q.pop(0)

        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny<M and lst[nx][ny] != 0 and visited[nx][ny] == 0 :
                Q.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1

    return visited[N-1][M-1]

N,M = map(int,input().split())

lst = [list(map(int,input())) for _ in range(N)]

print(maze(0,0))
