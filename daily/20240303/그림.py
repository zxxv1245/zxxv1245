def bfs() :
    global maxV
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    v = 0
    while Q :
        x,y = Q.popleft()
        lst[x][y] = 0
        v += 1
        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny<M and lst[nx][ny] == 1 :
                Q.append((nx,ny))
                lst[nx][ny] = 0


    maxV = max(maxV,v)


from collections import deque


N,M = map(int,input().split())

lst = [list(map(int,input().split()))for _ in range(N)]
Q = deque()
cnt = 0
maxV = 0
for i in range(N) :
    for j in range(M) :
        if lst[i][j] == 1 :
            Q.append((i,j))
            bfs()
            cnt += 1

print(cnt)
print(maxV)