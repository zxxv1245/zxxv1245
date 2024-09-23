lst = [[0]*101 for _ in range(101)]

for _ in range(4) :
    ax,ay,bx,by = map(int,input().split())

    for x in range(ax,bx) :
        for y in range(ay,by) :
            lst[x][y] += 1

cnt = 0
for i in range(101) :
    for j in range(101) :
        if lst[i][j] != 0 :
            cnt += 1

print(cnt)