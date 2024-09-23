from collections import deque

def bfs(k,i,j) :

    visited = [[[0]*M for _ in range(N)]for _ in range(H)]
    visited[k][i][j] = 1
    Q = deque()
    Q.append((k,i,j))
    while Q :
        h,x,y = Q.popleft()

        for nx,ny,nh in [(x+1,y,h),(x-1,y,h),(x,y+1,h),(x,y-1,h),(x,y,h-1),(x,y,h+1)] :
            if 0<=nx<N and 0<=ny<M and 0<=nh<H:
                if lst[nh][nx][ny] == '.' and visited[nh][nx][ny] == 0 :
                    visited[nh][nx][ny] = visited[h][x][y] + 1
                    Q.append((nh,nx,ny))
                elif lst[nh][nx][ny] == 'E' :
                    return f'Escaped in {visited[h][x][y]} minute(s).'

    return 'Trapped!'

while True :
    H,N,M = map(int,input().split())
    if H == 0 and N == 0 and M == 0 :
        break
    lst = []
    for _ in range(H) :
        lst.append([list(input()) for _ in range(N)])
        a = input()

    for k in range(H) :
        for i in range(N) :
            for j in range(M) :
                if lst[k][i][j] == 'S' :
                    sk,sx,sy = k,i,j

    print(bfs(sk,sx,sy))