
def check(ck) :
    if len(ck) == 0 :
        return False
    if len(ck) == 1 :
        return True
    Q = []
    Q.append(ck[0])
    # print(Q)
    ans = []
    while Q :
        x = Q.pop(0)

        for a in G[x] :
            if a in ck :
                if a not in ans :
                    Q.append(a)
                    ans.append(a)
    ans.sort()
    # print(ans)
    if ans == ck :
        return True
    else :
        return False
def dfs(k) :
    global minV
    if k == N+1 :
        ret1 = []
        ret2 = []
        for i in range(1,N+1) :
            if vt[i] == 0:
                ret1.append(i)
            else :
                ret2.append(i)
        # print(ret1)
        # print(ret2)
        # print()
        if check(ret1) and check(ret2) :
            sum1 = 0
            sum2 = 0
            for z in ret1 :
                sum1 += lst[z]
            for c in ret2 :
                sum2 += lst[c]
            ret = abs(sum1-sum2)
            if minV > ret :
                minV = ret
        return

    for i in range(2):
        vt[k] = i
        dfs(k+1)
        vt[k] = -1


from itertools import combinations
N = int(input())
lst = [-10]+list(map(int,input().split()))
G = [[] for _ in range(N+1)]

for a in range(1,N+1) :
    arr = list(map(int,input().split()))
    for b in range(1,arr[0]+1) :
        G[a].append(arr[b])
# print(G)
minV = 21e8
vt = [-1]+[0]*N
dfs(1)
if minV == 21e8 :
    print(-1)
else :
    print(minV)
