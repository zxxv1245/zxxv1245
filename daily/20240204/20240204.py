T = int(input())

for tc in range(1, T+1) :
    N,M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    maxV = 10000000000

    for i in range(N) :
        for j in range(M) :
            sumV = arr[i][j]
            for x in range(4) :
                ni = i + di[x]
                nj = j + dj[x]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += arr[i+di[x]][j+dj[x]]
            if maxV > sumV :
                maxV = sumV

    print(maxV)