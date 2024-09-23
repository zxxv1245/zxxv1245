import sys
input = sys.stdin.readline
N = int(input())
lst = [0]*8001
slst = set()
sumV = 0
maxV = -21e8
minV = 21e8
for _ in range(N) :
    V = int(input())
    maxV = max(maxV,V)
    minV = min(minV,V)
    sumV += V
    slst.add(V)
    lst[V+4000] += 1

ret1 = round(sumV/N,0)
slst = list(slst)
ret2 = slst[len(slst)//2]
ret3 = lst.index(max(lst))-4000
ret4 = maxV-minV
print(ret1)
print(ret2)
print(ret3)
print(ret4)