from collections import deque

import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs() :
    while Q :
        x,y = Q.popleft()
        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<= nx < N and 0<= ny < M and lst[nx][ny] == 0  :
                Q.append((nx,ny))
                lst[nx][ny] = lst[x][y] + 1
    maxV = 1
    for i in range(N) :
        for j in range(M) :
            if lst[i][j] == 0 :
                return -1
            elif maxV < lst[i][j] :
                maxV = lst[i][j]
    return maxV-1

M,N = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]
Q = deque()
for x in range(N) :
    for y in range(M) :
        if lst[x][y] == 1 :
            Q.append((x,y))

print(bfs())
