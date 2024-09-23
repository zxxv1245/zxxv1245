from collections import deque
import sys
input = sys.stdin.readline

xy = [1,-1]
def check(x0,y0,x1,y1,x2,y2) :
    if x0 == x1 and x1 == x2 :
        for a in range(2) :
            nx0,nx1,nx2 = x0 + xy[a], x1 + xy[a], x2 + xy[a]
            if 0 > nx0 or nx0 >= N or 0 > nx1 or nx1 >= N or 0 > nx2 or nx2 >= N :
                return False
            if lst[nx0][y0] == '1' or lst[nx1][y1] == '1' or lst[nx2][y2] == '1' :
                return False
        return 'C'
    elif y0 == y1 and y1 == y2 :
        for a in range(2):
            ny0, ny1, ny2 = y0 + xy[a], y1 + xy[a], y2 + xy[a]
            if 0 > ny0 or ny0 >= N or 0 > ny1 or ny1 >= N or 0 > ny2 or ny2 >= N :
                return False
            if lst[x0][ny0] == '1' or lst[x1][ny1] == '1' or lst[x2][ny2] == '1':
                return False
        return 'R'


def bfs() :

    visited = set()
    visited.add((Blst[0][0],Blst[0][1],Blst[1][0],Blst[1][1],Blst[2][0],Blst[2][1]))
    Q = deque()
    dem = []
    for i,j in Blst :
        dem.append(i)
        dem.append(j)
    dem.append(1)
    Q.append(dem)

    while Q :
        x0,y0,x1,y1,x2,y2,v = Q.popleft()
        # print(x0,y0,x1,y1,x2,y2,v)

        if x0 == Elst[0][0] and y0 == Elst[0][1] and x1 == Elst[1][0] and y1 == Elst[1][1] and x2 == Elst[2][0] and y2 == Elst[2][1] :
            return v - 1
            # 회전 회오리
        ck = check(x0, y0, x1, y1, x2, y2)
        if ck == 'R':  # 가로로 돌리기
            nx0, ny0, nx1, ny1, nx2, ny2 = x1, y1 - 1, x1, y1, x1, y1 + 1
            if 0 <= nx0 < N and 0 <= ny0 < N and 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
                if (nx0, ny0, nx1, ny1, nx2, ny2) not in visited :
                    visited.add((nx0, ny0, nx1, ny1, nx2, ny2))
                    Q.append((nx0, ny0, nx1, ny1, nx2, ny2, v + 1))
        elif ck == 'C':  # 세로로 돌리기
            nx0, ny0, nx1, ny1, nx2, ny2 = x1 - 1, y1, x1, y1, x1 + 1, y1
            if 0 <= nx0 < N and 0 <= ny0 < N and 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
                if (nx0, ny0, nx1, ny1, nx2, ny2) not in visited:
                    visited.add((nx0, ny0, nx1, ny1, nx2, ny2))
                    Q.append((nx0, ny0, nx1, ny1, nx2, ny2, v + 1))

        # 상 하 좌 우 체크
        for a in range(4) :
            nx0,ny0,nx1,ny1,nx2,ny2 = x0+dx[a],y0+dy[a],x1+dx[a],y1+dy[a],x2+dx[a],y2+dy[a]
            if 0<= nx0 < N and 0<= ny0 < N and 0<= nx1 < N and 0<= ny1 < N and 0<= nx2 < N and 0<= ny2 < N :
                if lst[nx0][ny0] != '1' and lst[nx1][ny1] != '1' and lst[nx2][ny2] != '1':
                    if (nx0, ny0, nx1, ny1, nx2, ny2) not in visited:
                        visited.add((nx0, ny0, nx1, ny1, nx2, ny2))
                        Q.append((nx0,ny0,nx1,ny1,nx2,ny2,v+1))

    return 0

N = int(input())

lst = [list(input()) for _ in range(N)]


Blst = []
Elst = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for i in range(N) :
    for j in range(N) :
        if lst[i][j] == 'B' :
            Blst.append((i,j))
        if lst[i][j] == 'E' :
            Elst.append((i,j))

print(bfs())

