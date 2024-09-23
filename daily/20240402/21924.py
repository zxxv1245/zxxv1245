import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
def findB(k) :
    if group[k] != k :
        group[k] = findB(group[k])
        return group[k]
    return k
def union(i,j) :
    global groups
    i,j = findB(i),findB(j)

    if i == j : return
    if i < j :
        group[j] = i
        groups -= 1
    else :
        group[i] = j
        groups -= 1
N,M = map(int,input().split())

ret = 0
lst = []
for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    lst.append((v1,v2,cost))
    ret += cost

lst.sort(key = lambda x:x[2],reverse=True)
group = [i for i in range(N+1)]
cnt = 0
total = 0
groups = N
while lst :
    v1,v2,cost = lst.pop()
    if findB(v1) != findB(v2) :
        total += cost
        union(v1,v2)

if groups >= 2 :
    print(-1)
else :
    print(ret - total)