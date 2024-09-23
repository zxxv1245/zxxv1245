from collections import deque
import sys
input = sys.stdin.readline
def bfs(sx,sy) :
    visited[0][0][0][0][0][0][sx][sy] = 1
    Q = deque()
    Q.append((0,0,0,0,0,0,sx,sy))

    while Q :
        a,b,c,d,e,f,x,y = Q.popleft()

        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            if 0<=nx<N and 0<=ny<M and lst[nx][ny] != '#' :
                if lst[nx][ny] == '.' and visited[a][b][c][d][e][f][nx][ny] == 0 :
                    visited[a][b][c][d][e][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                    Q.append((a,b,c,d,e,f,nx,ny))
                elif lst[nx][ny] in ['a','b','c','d','e','f'] and visited[a][b][c][d][e][f][nx][ny] == 0:
                    if lst[nx][ny] == 'a' :
                        na = 1
                        visited[na][b][c][d][e][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((na,b,c,d,e,f,nx,ny))
                    elif lst[nx][ny] == 'b' :
                        nb = 1
                        visited[a][nb][c][d][e][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((a,nb,c,d,e,f,nx,ny))
                    elif lst[nx][ny] == 'c' :
                        nc = 1
                        visited[a][b][nc][d][e][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((a,b,nc,d,e,f,nx,ny))
                    elif lst[nx][ny] == 'd' :
                        nd = 1
                        visited[a][b][c][nd][e][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((a,b,c,nd,e,f,nx,ny))
                    elif lst[nx][ny] == 'e' :
                        ne = 1
                        visited[a][b][c][d][ne][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((a,b,c,d,ne,f,nx,ny))
                    elif lst[nx][ny] == 'f' :
                        nf = 1
                        visited[a][b][c][d][e][nf][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((a,b,c,d,e,nf,nx,ny))
                elif lst[nx][ny] in ['A','B','C','D','E','F'] and visited[a][b][c][d][e][f][nx][ny] == 0:
                    if lst[nx][ny] == 'A' and a == 1:
                        visited[a][b][c][d][e][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((a, b, c, d, e, f, nx, ny))
                    elif lst[nx][ny] == 'B' and b == 1:
                        visited[a][b][c][d][e][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((a, b, c, d, e, f, nx, ny))
                    elif lst[nx][ny] == 'C' and c == 1:
                        visited[a][b][c][d][e][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((a, b, c, d, e, f, nx, ny))
                    elif lst[nx][ny] == 'D' and d == 1:
                        visited[a][b][c][d][e][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((a, b, c, d, e, f, nx, ny))
                    elif lst[nx][ny] == 'E' and e == 1:
                        visited[a][b][c][d][e][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((a, b, c, d, e, f, nx, ny))
                    elif lst[nx][ny] == 'F' and f == 1:
                        visited[a][b][c][d][e][f][nx][ny] = visited[a][b][c][d][e][f][x][y] + 1
                        Q.append((a, b, c, d, e, f, nx, ny))
                if lst[nx][ny] == '1':
                    return visited[a][b][c][d][e][f][x][y]
    return -1
N,M = map(int,input().split())
lst = [list(input()) for _ in range(N)]
visited = [[[[[[[[0]*M for _ in range(N)]for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(2)]
for i in range(N) :
    for j in range(M) :
        if lst[i][j] == '0' :
            sx,sy = i,j
            lst[i][j] = '.'
print(bfs(sx,sy))
