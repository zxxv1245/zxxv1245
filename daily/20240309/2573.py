from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs() :

    check = [[0]*M for _ in range(N)]
    while Q :
        x,y = Q.popleft()

        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny<M and lst[nx][ny] == 0 :
                check[x][y] += 1
            elif 0<=nx<N and 0<=ny<M and lst[nx][ny] != 0 and visited[nx][ny] == 0:
                Q.append((nx,ny))
                visited[nx][ny] = 1
    for i in range(N) :
        for j in range(M) :
            if check[i][j] != 0 :
                lst[i][j] -= check[i][j]
                if lst[i][j] < 0 :
                    lst[i][j] = 0
    # for j in check :
    #     print(*j)
    # for i in lst :
        # print(*i)

N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]
Q = deque()
ans = 0
cnt = 0
for i in range(N) :
    for j in range(M) :
        if lst[i][j] != 0 :
            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1
            Q.append((i,j))
            bfs()
            cnt += 1

            counting = 0
            for x in range(N) :
                for y in range(M) :
                    if lst[x][y] != 0 and visited[x][y] == 0 :
                        counting += 1

            if counting >= 1 :
                ans = 1
                break
    if ans == 1 :
        break
if ans == 1 :
    print(cnt-1)
else :
    print(0)