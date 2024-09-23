def findB(k) :
    if group[k] == k :
        return k
    ret = findB(group[k])

    return ret
def union(i,j,x) :
    global cnt,total
    fi,fj = findB(i),findB(j)
    if fi == fj :
        return

    total += arr[x][2]
    cnt += 1

    group[fj] =fi

T = int(input())
for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))
    start = lst[:2]
    end = lst[2:4]
    # lst = lst[4:]

    arr = []
    for i in range(N-1) :
        for j in range(i+1,N) :
            arr.append((i,j,abs(lst[2*i]-lst[2*j])+abs(lst[2*i+1]-lst[2*j+1])))

    arr.sort(key = lambda x:x[2])
    group = [i for i in range(N)]

    total = 0
    cnt = 0
    for x in range(len(arr)) :
        if cnt == N-1 :
            break
        union(arr[x][0],arr[x][1],x)

    print(total)
