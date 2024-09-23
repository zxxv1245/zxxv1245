import sys
input = sys.stdin.readline

N,M = map(int,input().split())

lst = [input() for _ in range(N)]

maxV = 0

for i in range(N-2) :
    for j in range(i+1, N-1) :
        cnt = 0
        for k in range(i+1) :
            cnt += lst[k].count('W')
        for k in range(i+1, j+1) :
            cnt += lst[k].count('B')
        for k in range(j+1, N) :
            cnt += lst[k].count('R')
        if maxV < cnt :
            maxV = cnt

print(N*M - maxV)