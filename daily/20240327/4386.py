import math
def findB(k) :
    if group[k] == k :
        return k
    group[k] = findB(group[k])
    return group[k]

def union(i,j) :
    global cnt,total
    fi,fj = findB(i),findB(j)


    group[fj] = fi


N = int(input())
lst = [list(map(float, input().split())) for _ in range(N)]
arr = []
for i in range(N-1) :
    for j in range(i+1,N) :

        arr.append((i,j,math.sqrt((lst[i][0]-lst[j][0])**2 + (lst[i][1]-lst[j][1])**2)))

arr.sort(key = lambda x:x[2])

group = [w for w in range(N)]
cnt = 0
total = 0
for x,y,cost in arr :
    if findB(x) != findB(y):
        union(x,y)
        total += cost



print(f'{total:.2f}')