
T = int(input())

for Test in range(1,T+1) :
    N,M = map(int,input().split())
    lst = [[0]*(N+1)for _ in range(N+1)]

    lst[N//2][N//2] = 2
    lst[N//2 +1][N//2 +1] = 2
    lst[N//2][N//2 +1] = 1
    lst[N//2 +1][N//2] = 1

    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]
    for r in range(M) :
        x,y,d = map(int,input().split())

              

    cntB = 0
    cntW = 0

    for i in range(N+1) :
        for j in range(N+1) :
            if lst[i][j] == 1 :
                cntB += 1
            elif lst[i][j] == 2 :
                cntW += 1

    print(f'#{Test} {cntB} {cntW}')