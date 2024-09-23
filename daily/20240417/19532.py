def findB(k) :
    if G[k] == k :
        return k
    ret = findB(G[k])
    G[k] = ret
    return ret
def union(x,y) :
    fx,fy = findB(x),findB(y)

    if fx == fy :
        return

    G[fy] = fx


N,M = map(int,input().split())
G = [i for i in range(N+1)]

for _ in range(M) :
    d,x,y = map(int,input().split())

    if d == 0 :
        union(x,y)
    elif d == 1 :
        if findB(x) == findB(y) :
            print('YES')
        else :
            print('NO')