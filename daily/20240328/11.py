def findB(k) :
    global cnt
    if group[k] == k :

        return k

    ret = findB(group[k])
    cnt += 1
    return ret

def union(i,j) :
    fi,fj = findB(i),findB(j)

    if fi == fj : return

    group[fj] =group[fi]



T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    friend = []
    group = [i for i in range(N*2)]
    for  _ in range(N) :
        cnt = 0
        a,b = input().split()
        if a not in friend :
            friend.append(a)
        if b not in friend:
            friend.append(b)
        union(friend.index(a),friend.index(b))
        findB(friend.index(a))
        findB(friend.index(b))
        # if friend.index(a) in group:
        #     findB(friend.index(b))
        print(cnt)
        # print(group.count(group[friend.index(b)]))
    print(group)