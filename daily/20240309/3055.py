from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs() :

    while Q :
        x,y,v = Q.popleft()
        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]

            if 0<=nx<N and 0<=ny<M :
                if v == 'S' :
                    if nx == gx and ny == gy and lst[x][y] != '*':
                        return lst[x][y]

                    if lst[nx][ny] == '.' and lst[x][y] != '*' :
                        Q.append((nx,ny,'S'))
                        lst[nx][ny] = lst[x][y] + 1
                elif v == '*' :
                    if lst[nx][ny] not in ['X','D','*']:
                        Q.append((nx,ny,'*'))
                        lst[nx][ny] = '*'
    return "KAKTUS"

N,M = map(int,input().split())
lst = [list(input()) for _ in range(N)]
hedgehog = deque()
water = deque()
Q = deque()

for i in range(N) :
    for j in range(M) :
        if lst[i][j] == 'S' :
            hedgehog.append((i,j))
            lst[i][j] = 1
        if lst[i][j] == '*' :
            water.append((i,j))
            lst[i][j] = '*'
        if lst[i][j] == 'D' :
            gx,gy = i,j

x,y = hedgehog.popleft()
Q.append((x,y,'S'))
if water :
    for (x,y) in water :
        Q.append((x,y,'*'))

print(bfs())