from itertools import combinations

def findB(k) :
    if group[k] == k :
        return k
    ret = findB(group[k])
    return ret
def union(i,j,x) :
    global cnt,total
    fi,fj = findB(i),findB(j)

    if fi == fj : return

    cnt += 1
    total += ck[x][2]

    group[fj] = fi

lst = [list(input()) for _ in range(5)]
arr = [(0,0),(0,1),(0,2),(0,3),(0,4),
       (1,0),(1,1),(1,2),(1,3),(1,4),
       (2,0),(2,1),(2,2),(2,3),(2,4),
       (3,0),(3,1),(3,2),(3,3),(3,4),
       (4,0),(4,1),(4,2),(4,3),(4,4)]

ans = list(combinations(arr,7))
result = 0
ansA = []
for x in ans :
    aa = []
    for y in x :
        aa.append(lst[y[0]][y[1]])
    if aa.count('S') >= 4 :
        ansA.append(x)
for combi in ansA :
    ck = []
    for i in range(6) :
        for j in range(i+1,7) :
            ck.append((i,j,abs(combi[i][0]-combi[j][0])+abs(combi[i][1]-combi[j][1])))
    ck.sort(key = lambda x:x[2])
    cnt = 0
    total = 0
    group = [i for i in range(7)]
    for x in range(len(ck)) :
        if cnt == 6 :
            break
        union(ck[x][0],ck[x][1],x)
    if total == 6 :
        result += 1

print(result)