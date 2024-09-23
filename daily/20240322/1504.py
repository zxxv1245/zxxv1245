from heapq import heappop,heappush

def dijkstra() :

    while heap :
        cost,ky = heappop(heap)

        if cost > result[ky]  : continue

        for next_cost,next in G[ky] :
            prev = result[next]
            new_cost = cost + next_cost

            if prev > new_cost :
                result[next] = new_cost
                heappush(heap,(new_cost,next))


N,E = map(int,input().split())
G = [[] for _ in range(N+1)]
for _ in range(E) :
    v1,v2,w = map(int,input().split())
    G[v1].append((w,v2))
    G[v2].append((w,v1))
ky1,ky2 = map(int,input().split())

result = [21e8]*(N+1)
result[1] = 0
heap = [(0,1)]
dijkstra()
# print(result)
ret1 = result[ky1]
ret2 = result[ky2]

result = [21e8] * (N + 1)
result[ky1] = 0
heap = [(0, ky1)]
dijkstra()
ret1 += result[ky2]
result = [21e8] * (N + 1)
result[ky2] = 0
heap = [(0, ky2)]
dijkstra()
ret1 += result[N]


    # print(ret)
result = [21e8] * (N + 1)
result[ky2] = 0
heap = [(0, ky2)]
dijkstra()
# print(result)
ret2 += result[ky1]
# print(ret)
result = [21e8] * (N + 1)
result[ky1] = 0
heap = [(0, ky1)]
dijkstra()
# print(result)
ret2 += result[N]
ret = min(ret1,ret2)
    # print(ret)
if ret >= 21e8  :
    print(-1)
else :
    print(ret)