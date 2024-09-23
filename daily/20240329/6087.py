from heapq import heappush,heappop
import sys
input = sys.stdin.readline
INF = sys.maxsize


N,M,X,Y = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
    G[v2].append((cost,v1))

result = [INF]*N
result[Y] = 0
heap = [(0,Y)]

while heap :
    cost,ky = heappop(heap)

    if cost > result[ky] : continue

    for next_cost,next in G[ky] :
        prev = result[next]
        new_cost = cost + next_cost
        if prev > new_cost :
            result[next] = new_cost
            heappush(heap,(new_cost,next))

result.sort()

a = X
cnt = 1
for i in result :
    if i > X  :
        cnt = -1
        break
    na = a - i*2
    if na < 0 :
        a = X
        cnt += 1
    a -= i*2
print(cnt)