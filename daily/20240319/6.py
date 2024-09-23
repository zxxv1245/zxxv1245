def finB(k) :
    if group[k] == 0 :
        return k
    ret = finB(group[k])
    group[k] = ret
    return ret



def union(i,j) :
    fi,fj = findB(i),findB(j)
    if fi == fj :
        return

    group[fj] = fi
T = int(input())
for Test in range(1,T+1) :
    N,M= map(int,input().split())
    lst = list(map(int,input().split()))
    group = [0]*(N+1)
    for i in range(0,M*2,2) :
        union(lst[i],lst[i+1])

    cnt = 0
    for i in group[1:] :
        if i == 0 :
            cnt += 1
    print(f'#{Test} {cnt}')