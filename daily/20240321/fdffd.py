from heapq import heappop,heappush

T = int(input())
for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))



    arr = [[]for _ in range(N+2)]
    for i in range(N+1) :
        for j in range(i+1,N+2) :
            arr[i].append((abs(lst[2*i]-lst[2*j])+abs(lst[2*i+1]-lst[2*j+1]),j))
            arr[j].append((abs(lst[2*i]-lst[2*j])+abs(lst[2*i+1]-lst[2*j+1]),i))
    result = [21e8]*(N+2)
    result[0] = 0
    heap = [(0,0)]

    while heap :
        cost,ky = heappop(heap)

        if cost > result[ky] : continue

        for next_cost,next in arr[ky] :
            prev = result[next]
            new_cost =cost + next_cost

            if prev > new_cost :
                result[next] = new_cost
                heappush(heap,(new_cost,next))

    print(result)