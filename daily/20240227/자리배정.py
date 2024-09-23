C,R = map(int,input().split())
k = int(input())

lst = [[0]*R for _ in range(C)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
x = 0
y = 0
a = 0
i = 1
lst[x][y] = 1
if k > C*R :
    print(0)
else :
    while i < k :
        nx = x + dx[a]
        ny = y + dy[a]
        if 0<=nx<C and 0<=ny<R and lst[nx][ny] == 0 :
            lst[nx][ny] = i+1
            x,y = nx,ny
            i += 1
        else :
            a = (a+1) % 4

    print(x+1, y+1)
