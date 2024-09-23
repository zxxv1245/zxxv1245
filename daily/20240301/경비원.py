def bfs(x,y) :
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    Q = []
    ret = 0
    visited = [[0]*(W+1) for _ in range(H+1)]
    Q.append([x,y])
    visited[x][y] = 1
    while True :
        x,y = Q.pop(0)
        if lst[x][y] in list(range(1,N+1)) :
            ret += visited[x][y] -1
        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < H+1 and 0<= ny < W+1 and lst[nx][ny] != 'X' and visited[nx][ny] == 0 :
                visited[nx][ny] = visited[x][y] + 1
                Q.append([nx,ny])

        if not Q :
            return ret


W,H = map(int,input().split())
N = int(input())
lst = [[0]*(W+1) for _ in range(H+1)]

for a in range(1,H) :
    for b in range(1,W) :
        lst[a][b] = 'X'

for i in range(1,N+1) :
    A, xy = map(int,input().split())
    if A == 1 :
        lst[0][xy] = i
    elif A == 2 :
        lst[H][xy] = i
    elif A == 3 :
        lst[xy][0] = i
    elif A == 4 :
        lst[xy][W] = i

A, xy = map(int,input().split())
if A == 1 :
    lst[0][xy] = 'M'
    x = 0
    y = xy
elif A == 2 :
    lst[H][xy] = 'M'
    x = H
    y = xy
elif A == 3 :
    lst[xy][0] = 'M'
    x = xy
    y = 0
elif A == 4 :
    lst[xy][W] = 'M'
    x = xy
    y = W

for i in lst :
    print(*i)

print(bfs(x,y))


