from heapq import heappop,heappush

def dijkstra(i) :
    result = [21e8] * (N + 1)
    result[i] = 0
    heap = [(0, i)]

    while heap :
        weight, ky = heappop(heap)

        if weight > result[ky] : continue

        for next_weight, next in G[ky] :
            prev = result[next]
            new_weight = weight + next_weight

            if prev > new_weight :
                result[next] = new_weight
                heappush(heap, (new_weight,next))
    return result[1:]

N,M,R = map(int,input().split())
item = list(map(int,input().split()))
G= [[] for _ in range(N+1)]
for _ in range(R) :
    v1,v2,weight = map(int,input().split())
    G[v1].append((weight,v2))
    G[v2].append((weight,v1))
maxV = -21e8
for i in range(1,N+1) :
    ret = dijkstra(i)
    ans = 0
    for j in range(N) :
        if ret[j] <= M :
            ans += item[j]
    if maxV < ans :
        maxV = ans

print(maxV)