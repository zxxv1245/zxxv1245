from collections import  deque

def bfs() :

    Q = deque()
    Q.append((sx,sy,1000))

    while Q :
        x,y,k = Q.popleft()
        if x == ex and y == ey and k >= 0 :
            return 'happy'
        for nx,ny in [(x+50,y),(x,y+50)] :
            pass

T = int(input())
for _ in range(1,T+1) :
    N = int(input())
    sx,sy = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]
    ex,ey = map(int,input().split())
    bfs()