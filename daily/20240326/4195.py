def findB(k) :
    
    if group[k] == k :
        return k
    ret = findB(group[k])
    group[k] = ret
    return ret

def union(i,j) :
    fi,fj = findB(i),findB(j)

    if fi == fj : return

    group[fj] = fi




T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    friend = []
    group = [i for i in range(N*2)]
    for  _ in range(N) :
        a,b = input().split()
        if a not in friend :
            friend.append(a)
        if b not in friend:
            friend.append(b)
        union(friend.index(a),friend.index(b))

        print(group)
        print(group.count(group[friend.index(b)]))
