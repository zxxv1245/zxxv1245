x = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
xA = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D' , 4 : 'E', 5 : 'F', 6 : 'G' , 7 : 'H'}
move = {'R' : 0, 'RB' : 1, 'B' : 2, 'LB' : 3, 'L' : 4, 'LT' : 5, 'T' : 6, 'RT' : 7}
lst = [[0]*8 for _ in range(8)]

K,D,N = input().split()

lst[8-int(K[1])][x[K[0]]] = 1
kx = 8-int(K[1])
ky = x[K[0]]
lst[8-int(D[1])][x[D[0]]] = 2
ax = 8-int(D[1])
ay = x[D[0]]
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]
for _ in range(int(N)) :
    m = input()
    m = move[m]
    nx = kx + dx[m]
    ny = ky + dy[m]
    nnx = ax + dx[m]
    nny = ay + dy[m]
    if 0<=nx<8 and 0<=ny<8:
        if 0<=nnx<8 and 0<=nny<8 and nx == ax and ny == ay:
                lst[nnx][nny] = 2
                lst[ax][ay] = 0
                ax = nnx
                ay = nny
        if lst[nx][ny] == 0 :
            lst[kx][ky] = 0
            lst[nx][ny] = 1
            kx = nx
            ky = ny
for i in range(8) :
    for j in range(8) :
        if lst[i][j] == 1:
            kx = i
            ky = j
        elif lst[i][j] == 2:
            ax = i
            ay = j
kx = 8-kx
ax = 8-ax
ky = xA[ky]
ay = xA[ay]
print(ky,end ='')
print(kx)
print(ay,end ='')
print(ax)