from heapq import heappush,heappop

def dijkstra() :

    distance = [[21e8]*N for _ in range(N)]
    distance[0][0] = lst[0][0]
    heap = [(lst[0][0],0,0)]

    while heap :
        cost,x,y = heappop(heap)
        if x == N -1 and y == N -1 :
            return cost
        for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<= i < N and 0<= j < N :
                cost = distance[x][y] + lst[i][j]
                if distance[i][j] > cost :
                    distance[i][j] = cost
                    heappush(heap, (distance[i][j],i,j))

Test = 1
while True :

    N = int(input())
    if N == 0 : break
    lst = [list(map(int,input().split())) for _ in range(N)]

    print(f'Problem {Test}: {dijkstra()}')
    Test += 1