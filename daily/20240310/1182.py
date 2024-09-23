import sys

input = sys.stdin.readline
def abc(k,path) :

    if k == M :
        ret.append(path)
        return
    prev = 0
    for i in range(N) :
        if v1[i] == 0 and prev != lst[i] :
            v1[i] = 1
            prev = lst[i]
            abc(k+1,path + [lst[i]])
            v1[i] = 0

N,M = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort()

ret = []
v1 = [0]*N

abc(0,[])

for i in ret :
    print(*i)



