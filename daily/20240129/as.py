T = int(input())

for Test in range(1,T+1) :
    N,M = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]

    maxV = -21e8
    for i in range(N) :
        cnt = 0
        for j in range(M) :
            if lst[i][j] == 1 :
               cnt += 1
            else :
                if maxV < cnt :
                    maxV = cnt
                cnt = 0
        if maxV < cnt :
            maxV = cnt

    for i in range(M):
        cnt = 0
        for j in range(N):
            if lst[j][i] == 1:
                cnt += 1
            else:
                if maxV < cnt:
                    maxV = cnt
                cnt = 0
        if maxV < cnt:
            maxV = cnt

    print(f'#{Test} {maxV}')