N = int(input())
lst = [[0]*101 for _ in range(101)]
for _ in range(N) :
    x, y = map(int,input().split())

    for i in range(x,x+10) :
        for j in range(y,y+10) :
            if lst[i][j] == 0 :
                lst[i][j] = 1

di = [0,1,0,-1]
dj = [1,0,-1,0]
cnt = 0
for i in range(100) :
    for j in range(100) :
        if lst[i][j] == 1 :
            for a in range(4) :
                ni = i + di[a]
                nj = j + dj[a]
                if 0<=ni<101 and 0<=nj<101 and lst[ni][nj] == 0:
                    cnt += 1


print(cnt)

