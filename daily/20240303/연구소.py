import copy
from collections import deque
def bfs(Q) :
    global maxV
    arr = copy.deepcopy(lst)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while Q :
        x,y = Q.popleft()
        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0 :
                arr[nx][ny] = 2
                Q.append((nx,ny))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
    if maxV < cnt:
        maxV = cnt


def abc(k) :
    if k == 3 :
        Q= deque()
        for x in range(N):
            for y in range(M):
                if lst[x][y] == 2:
                    Q.append((x, y))

        bfs(Q)

        return

    for i in range(N) :
        for j in range(M) :
            if lst[i][j] == 0 and used[i][j] == 0 :
                lst[i][j] = 1
                used[i][j] = 1
                abc(k+1)
                lst[i][j] = 0
                used[i][j] = 0



N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]
used = [[0]*M for _ in range(N)]
maxV = -21e8
abc(0)
print(maxV)
