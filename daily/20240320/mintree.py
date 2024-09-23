def findB(k) :
    if group[k] == k :
        return k
    ret = findB(group[k])
    group[k] = ret
    return ret

def union(x,y,i) :
    global total,cnt
    fx,fy = findB(x),findB(y)
    if fx == fy :
        return
    total += lst[i][2]
    cnt += 1
    group[fy] = fx


T = int(input())

for Test in range(1,T+1) :
    V,E = map(int,input().split())
    group = [i for i in range(V+1)]
    lst = [list(map(int,input().split())) for _ in range(E)]

    lst.sort(key = lambda x : x[2])

    cnt = 0
    total = 0
    for i in range(E) :
        if cnt == V :
            break
        union(lst[i][0],lst[i][1],i)
    print(f'#{Test} {total}')
