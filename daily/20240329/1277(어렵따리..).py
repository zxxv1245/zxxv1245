from heapq import heappush,heappop
import sys
input = sys.stdin.readline
INF = sys.maxsize
from math import sqrt

def dijkstra() :

    while heap :
        cost,ky = heappop(heap)

        if cost > result[ky] : continue

        for next_cost,next in G[ky] :
            prev = result[next]
            new_cost = cost + next_cost
            if prev > new_cost :
                result[next] = new_cost
                heappush(heap,(new_cost,next))


N,W = map(int,input().split())
M = float(input())

lst = [list(map(int,input().split())) for _ in range(N)]
G = [[] for _ in range(N+1)]
for i in range(N-1) :
    for j in range(i+1,N) :
        G[i].append((sqrt((lst[i][0]-lst[j][0])**2 + (lst[i][1]-lst[j][1])**2),j))

result = [INF]*(N+1)
result[0] = 0
heap = [(0,0)]
dijkstra()
print(result)
ret = (result[N-1]-M)*1000
print(int(ret))