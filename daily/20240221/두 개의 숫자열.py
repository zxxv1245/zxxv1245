
T = int(input())

for Test in range(1,T+1) :
    N,M = map(int,input().split())
    if N > M :
        lstB = list(map(int,input().split()))
        lstA = list(map(int,input().split()))
        N, M = M, N
    else :
        lstA = list(map(int, input().split()))
        lstB = list(map(int, input().split()))

    maxV = -21e8
    for i in range(M-N+1):
        lstT = lstB[i:i+N]
        ret = 0
        for j in range(N):
            ret += lstT[j] * lstA[j]
        if maxV < ret :
            maxV = ret

    print(f'#{Test} {maxV}')