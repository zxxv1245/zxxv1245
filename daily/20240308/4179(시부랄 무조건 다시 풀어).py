from collections import deque
def bfs() :

    while fire :
        x,y = fire.popleft()

        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < r and 0 <= ny < c :
                if visited_f[nx][ny] == 0 and lst[nx][ny] != '#' :
                    fire.append((nx,ny))
                    visited_f[nx][ny] = visited_f[x][y] + 1
    while jihoon:
        x,y = jihoon.popleft()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < r and 0 <= ny < c :
                if lst[nx][ny] != '#' and visited_j[nx][ny] == 0:
                    if visited_f[nx][ny] == 0 or visited_f[nx][ny] > visited_j[x][y] + 1 :
                        jihoon.append((nx,ny))
                        visited_j[nx][ny] = visited_j[x][y] + 1
            else :
                return visited_j[x][y]
    return 'IMPOSSIBLE'

r,c = map(int,input().split())

lst = [list(input()) for _ in range(r)]
visited_j = [[0]*c for _ in range(r)]
visited_f = [[0]*c for _ in range(r)]
jihoon = deque()
fire = deque()
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for i in range(r) :
    for j in range(c) :
        if lst[i][j] == 'J' :
            jihoon.append((i,j))
            visited_j[i][j] = 1
        elif lst[i][j] == 'F' :
            fire.append((i,j))
            visited_f[i][j] = 1

print(bfs())
