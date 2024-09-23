import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * 1001

maxH = -21e8
for _ in range(N) :
    L,H = map(int,input().split())

    lst[L] = H


for i in range(1000) :
    if maxH <= lst[i] :
        maxH = lst[i]
        idx = i


ret = 0
maxx = 0
cnt = 1
for a in range(0,idx+1) :
    if maxx <= lst[a] :
        ret += maxx * cnt

        maxx = lst[a]
        cnt = 0
    cnt += 1

maxx = 0
cnt = 1
for b in range(1000,idx-1,-1) :
    if maxx < lst[b]:
        ret += maxx * cnt

        maxx= lst[b]
        cnt = 0
    cnt += 1


print(ret + maxH)

