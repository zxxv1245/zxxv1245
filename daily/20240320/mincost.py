import heapq

def dijkstra() :
    heap = [(0, 0, 0)]
    visited = [[21e8] * N for _ in range(N)]
    visited[0][0] = 0
    while heap:
        cost, x, y = heapq.heappop(heap)
        if x == N - 1 and y == N - 1:
            return cost

        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= i < N and 0 <= j < N:
                new_cost = cost + 1
                if lst[i][j] - lst[x][y] > 0:
                    new_cost += (lst[i][j] - lst[x][y])
                if visited[i][j] > new_cost :
                    visited[i][j] = new_cost
                    heapq.heappush(heap, (visited[i][j], i, j))


T = int(input())
for Test in range(1,T+1) :
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{Test} {dijkstra()}')


