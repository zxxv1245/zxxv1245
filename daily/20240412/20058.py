from collections import deque

N,Q = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(2**N)]

for _ in range(Q) :
    L = int(input())
    # 배열 돌리기
    arr = [[0]*2**N for _ in range(2**N)]

    startx, starty = 0, 0

    while True :

        for x in range(startx,startx+2**L) :
            for y in range(starty,starty+2**L) :
                arr[startx+2**L-1-x][starty+2**L-1-y]=lst[y][x]
        startx,starty = startx,starty + 2**L
        if starty > 2**N :
            starty = 0
            startx += 2**L
        if startx > 2**N and starty > 2**N :
            break

    for i in range(2**N) :
        arr[i] = reversed(arr[i])













# 출력

def bfs(i,j) :
    global cnt
    visited = [[0]*(2**N) for _ in range(2**N)]
    visited[i][j] = 1
    Q = deque()
    Q.append((i,j))
    lst[i][j] = 0
    cnt = 1
    while Q :
        x,y = Q.popleft()

        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            if 0<= nx <2**N and 0<= ny < 2**N :
                if lst[nx][ny] >= 1 and visited[nx][ny] == 0 :
                    visited[nx][ny] = 1
                    lst[nx][ny] = 0
                    Q.append((nx,ny))
                    cnt += 1

    return cnt




result = 0
ret = -21e8
# 남은 얼음의 합
for i in range(2**N) :
    for j in range(2**N) :
        result += lst[i][j]

flag = 0
for i in range(2**N) :
    for j in range(2**N) :
        cnt = 0
        if lst[i][j] >= 1 :
            value = bfs(i,j)
            if ret < value :
                ret = value

print(result)
if ret == 1 :
    print(0)
else :
    print(ret)