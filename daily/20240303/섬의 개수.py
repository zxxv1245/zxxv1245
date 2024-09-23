from collections import deque

def bfs() :

    while Q :
        x,y = Q.popleft()

        for a in range(8) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny<M and lst[nx][ny] == 1 :
                Q.append((nx,ny))
                lst[nx][ny] = 0


dx = [-1,0,1,1,1,0,-1,-1]
dy = [1,1,1,0,-1,-1,-1,0]

while True :
    M,N = map(int,input().split())
    if M == 0 and N == 0 :
        break
    lst = [list(map(int,input().split())) for _ in range(N)]
    Q = deque()
    cnt = 0
    for x in range(N) :
        for y in range(M) :
            if lst[x][y] == 1 :
                Q.append((x,y))
                bfs()
                cnt += 1

    print(cnt)