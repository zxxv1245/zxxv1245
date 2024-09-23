import sys
input = sys.stdin.readline
def findB(k) :
    if group[k] == k :
        return k

    ret = findB(group[k])
    group[k] = ret
    return ret
def union(r,c,x) :
    global total,cnt
    fr,fc = findB(r),findB(c)

    if fr == fc : return

    cnt += 1
    total += arr[x][2]

    group[fc] = fr

N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]
arr = []
for i in range(N) :
    for j in range(N) :
        if i == j : continue
        arr.append((i,j,lst[i][j]))

arr.sort(key = lambda x:x[2])
group = [i for i in range(N+1)]
cnt = 0
total = 0
for x in range(len(arr)) :
    if cnt == N-1 :
        break

    union(arr[x][0],arr[x][1],x)

print(total)