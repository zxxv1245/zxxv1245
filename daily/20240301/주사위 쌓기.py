N = int(input())
arr = [5,3,4,1,2,0]
lst = [list(map(int,input().split())) for _ in range(N)]
maxV = -21e8
llst = []
for i in range(6) :
    llst = [[] for _ in range(N)]
    for r in range(N) :
        for c in range(6) :
            llst[r].append(lst[r][c])
    llst[0][i] = 0
    y = i
    for j in range(N-1) :
        value = llst[j][arr[y]]
        llst[j][arr[y]] = 0

        k = llst[j + 1].index(value)
        llst[j+1][k] = 0
        y = k
    llst[N-1][arr[y]] = 0
    sumV = 0
    for x in llst :
        sumV += max(x)

    maxV = max(maxV,sumV)

print(maxV)