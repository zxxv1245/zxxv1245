T = int(input())

for Test in range(1, T+1) :
    N,M = map(int, input().split())
    lst = [list(map(int, input().split()))for _ in range(N)]

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    maxV = 0

    for x in range(N):
        for y in range(M):
            sumV = lst[x][y]
            for a in range(4) :
                for b in range(1,lst[x][y]+1) :
                    nx = x + dx[a]*b
                    ny = y + dy[a]*b
                    if 0<=nx<N and 0<=ny<M :
                        sumV += lst[nx][ny]
            if maxV < sumV :
                maxV = sumV

    print(f'#{Test} {maxV}')