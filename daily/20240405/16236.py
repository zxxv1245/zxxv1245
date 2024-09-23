from collections import deque
# 마지막으로 물고기를 먹었을 때 nx,ny,level,cnt,ret 를 갱신 후 리턴
# 탐색 중 물고기를 먹으면 flag = True
# 탐색 중 물고기를 못먹으면 flag = False
# sx,sy 상어의 현재 좌표
# level 상어의 크기
# cnt 상어가 먹은 물고기 수
# ret 움직인 시간
def bfs() :
    global sx,sy,level,cnt,ret,flag
    visited = [[0]*N for _ in range(N)]
    visited[sx][sy] = 1
    Q = deque()
    Q.append((sx,sy,level,cnt,ret))

    while Q :
        x,y,lev,cn,re = Q.popleft()

        for a in range(4) :
            nx,ny = x+dx[a],y+dy[a]
            if 0<=nx<N and 0<=ny<N :
                if (lst[nx][ny] == 0 or lst[nx][ny] == lev) and visited[nx][ny] == 0 :
                    visited[nx][ny] = 1
                    Q.append((nx,ny,lev,cn,re+1))
                if 1<=lst[nx][ny]<lev and visited[nx][ny] == 0 :
                    sx,sy = nx,ny
                    level = lev
                    cnt = cn+1
                    ret = re+1
                    print(f'{lst[nx][ny]},nx = {nx}, ny = {ny}, ret = {ret}, level = {level}')
                    lst[nx][ny] = 0

                    return
    flag = 0
    return
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]

for i in range(N) :
    for j in range(N) :
        if lst[i][j] == 9 :
            sx,sy = i,j
            lst[i][j] = 0

flag = 1
level = 2
cnt = 0
ret = 0
while True :
    if flag == 0 :
        break
    if cnt == level :
        level += 1
        cnt = 0

    bfs()

print(ret)

