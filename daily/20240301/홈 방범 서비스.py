def profit_check(home,k,M) :
    global maxV
    profit = (M * home) - (k * k + (k - 1) * (k - 1))
    if profit >= 0 :
        if maxV < home :
            maxV = home

def check(x,y,N,M) :
    k = 1
    while k < N+4 :
        home = 0
        for i in range(N) :
            for j in range(N) :
                if lst[i][j] == 1:
                    dist = abs(i-x)+abs(j-y)+1
                    if dist <= k :
                        home += 1

        if home >= maxV :
            profit_check(home,k,M)

        k += 1


T = int(input())

for Test in range(1,T+1) :
    N,M = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]
    maxV = -21e8
    for x in range(N) :
        for y in range(N) :
            if x == 0 and y == 5 :
                a = x
            check(x,y,N,M)

    print(f'#{Test} {maxV}')