from collections import deque

def bfs() :

    Q = deque()
    Q.append((rx, ry, 'R', 0))
    Q.append((bx, by, 'B', 0))
    Q.append((rx, ry, 'R', 0))
    Q.append((bx, by, 'B', 0))




N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(N) :
    for j in range(M) :
        if lst[i][j] == 'R' :
            rx,ry = i,j
        elif lst[i][j] == 'B' :
            bx,by = i,j
        elif lst[i][j] == 'O' :
            ex,ey = i,j

result = 1 #결과값
turn = 0

red_cnt = 1
blue_cnt = 1
    # 1. 공을 움직일 수 있어야 함.

bfs()


print(result)