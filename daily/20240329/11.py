from heapq import heappop,heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
def dijkstra() :

    distance[0][0] = 0
    heap = [(0,0,0)]

    while heap :
        cost,x,y = heappop(heap)
        if x == N-1 and y == N-1 :
            return cost
        if cost > distance[x][y] : continue


        for i,j in [(x+1,y),(x,y+1)]:
            if 0<= i < N and 0 <= j < N :
                if lst[x][y] > lst[i][j] :
                    if distance[i][j] > cost :
                        distance[i][j] = cost
                        heappush(heap,(cost,i,j))
                elif lst[x][y] <= lst[i][j] :
                    new_cost = distance[x][y] + (lst[i][j]-lst[x][y])+1
                    if distance[i][j] > new_cost :
                        distance[i][j] = new_cost
                        heappush(heap,(new_cost,i,j))



N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]
distance = [[INF]*N for _ in range(N)]
print(dijkstra())
# for i in distance :
#     print(*i)
