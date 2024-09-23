from heapq import heappush,heappop

def dijkstra() :

    while heap :
        cost,x,y,vis = heappop(heap)
        if x == end[0] and y == end[1] and len(vis) == N :
            return cost
        for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            if 0<= i <= 100 and 0<= j <= 100 :
                if xlst[i][j] == 1 :
                    vis.add((i,j))
                cost = arr[x][y] + 1
                if arr[i][j] > cost :
                    arr[i][j] = cost
                    heappush(heap,(arr[i][j],i,j,vis))
T = int(input())
for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))
    arr = [[21e8]*101 for _ in range(101)]
    start = lst[:2]
    arr[start[0]][start[1]] = 0
    end = lst[2:4]
    lst = lst[4:]
    xlst = [[0] * 101 for _ in range(101)]
    for i in range(N) :
        xlst[lst[2*i]][lst[2*i+1]] = 1

    heap=[(0,start[0],start[1],set())]
    print(dijkstra())
