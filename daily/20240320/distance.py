import heapq

T = int(input())
for Test in range(1,T+1) :
    N,E = map(int,input().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(E) :
        v1,v2,cost = map(int,input().split())
        arr[v1].append((cost,v2))

    result = [21e8]*(N+1)
    result[0] = 0
    heap = [(0,0)]

    while heap :
        cost,ky = heapq.heappop(heap)

        if cost > result[ky] : continue

        for next_cost,next in arr[ky] :
            baro = result[next]
            new_cost = cost + next_cost

            if baro > new_cost :
                result[next] = new_cost
                heapq.heappush(heap,(new_cost,next))

    print(f'#{Test} {result[N]}')