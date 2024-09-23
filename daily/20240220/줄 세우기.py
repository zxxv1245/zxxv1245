import sys
input = sys.stdin.readline

N = int(input())
lst = [[0]*1001 for _ in range(1001)]
for a in range(1,N+1) :
    x,y,dx,dy = map(int,input().split())

    for i in range(x,x+dx) :
        for j in range(y,y+dy) :
            lst[i][j] = a

for x in range(1,N+1) :
    cnt = 0
    for i in range(1001) :
        for j in range(1001) :
            if lst[i][j] == x :
                cnt += 1
    print(cnt)