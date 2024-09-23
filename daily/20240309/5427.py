from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs() :

    while Q :
        x,y,v = Q.popleft()

        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny<M :
                if v == '@' and lst[x][y] != '#' and lst[nx][ny] == '.':
                    Q.append((nx,ny,'@'))
                    lst[nx][ny] = lst[x][y] + 1
                elif v == '*' and lst[nx][ny] != '#' :
                    Q.append((nx,ny,'*'))
                    lst[nx][ny] = '#'
            else :
                if v == '@' and lst[x][y] != '#' :
                    return lst[x][y]
    return "IMPOSSIBLE"

T = int(input())

for Test in range(1,T+1) :
    M,N = map(int,input().split())
    lst = [list(input()) for _ in range(N)]
    person = deque()
    fire = deque()
    Q = deque()

    for i in range(N) :
        for j in range(M) :
            if lst[i][j] == '@' :
                person.append((i,j))
                lst[i][j] = 1
            if lst[i][j] == '*' :
                fire.append((i,j))
                lst[i][j] = '#'

    x,y = person.popleft()
    Q.append((x,y,'@'))
    if fire :
        for (x,y) in fire :
            Q.append((x,y,'*'))

    print(bfs())
