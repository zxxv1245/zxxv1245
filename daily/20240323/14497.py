from collections import deque

def bfs() :

    visited = [[0]*M for _ in range(N)]
    Q = deque()
    Q.append((si-1,sj-1))
    visited[si-1][sj-1] = 1

    while Q :
        x,y = Q.popleft()
        for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if i == ei - 1 and j == ej - 1:
                return 1
            if 0<=i<N and 0<=j<M :
                if lst[i][j] == '1' :
                    lst[i][j] = '0'
                    visited[i][j] = 1
                if lst[i][j] == '0' and visited[i][j] == 0:
                    visited[i][j] = 1
                    Q.append((i,j))
    return 0
N,M = map(int,input().split())
si,sj,ei,ej = map(int,input().split())

lst = [list(input()) for _ in range(N)]

cnt = 0
while True :
    cnt += 1
    if bfs() :
        break


print(cnt)
