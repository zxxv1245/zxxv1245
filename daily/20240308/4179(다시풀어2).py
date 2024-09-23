def bfs() :

    while Q :
        x,y,v = Q.popleft()
        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if v == 'J' and not (0 <= nx < r and 0 <= ny < c):
                if lst[x][y] == '#':
                    continue
                return lst[x][y]
            elif 0 <= nx < r and 0 <= ny < c :
                if lst[nx][ny] != "#" and v == "F":
                    lst[nx][ny] = "#"
                    Q.append((nx, ny, "F"))
                elif lst[nx][ny] == "." and v == "J" and lst[x][y] != "#":
                    lst[nx][ny] = lst[x][y] + 1
                    Q.append((nx, ny, "J"))
    return "IMPOSSIBLE"

from collections import deque

r,c = map(int,input().split())

lst = [list(input()) for _ in range(r)]
jihoon = deque()
fire = deque()
Q = deque()
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for i in range(r) :
    for j in range(c) :
        if lst[i][j] == 'J' :
            jihoon.append((i,j))
            lst[i][j] = 1
        elif lst[i][j] == 'F' :
            fire.append((i,j))
            lst[i][j] = "#"


x,y = jihoon.popleft()
Q.append((x,y,'J'))
if fire :
    for (x,y) in fire :
        Q.append((x,y,'F'))

print(bfs())