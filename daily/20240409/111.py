from heapq import heappop,heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline


# dfs랑 dijkstra랑 합쳐야함
# dijkstra 한번으로 모든 경로를 구해야함
# def dfs(x,k,sumV) :
#     global minD,mind
#     if k > minD :
#         return
#     if  x == e :
#         if mind > k :
#             mind = k
#         ret.append([sumV,k])
#         return
#
#     for cost,ky in G[x] :
#         if visited[ky] != 1 :
#             visited[ky] = 1
#             dfs(ky,k+1,sumV+cost)
#             visited[ky] = 0
def dijkstra() :

    result = [[INF]*(N+1) for _ in range(N+1)] # x = 해당 노드까지 최단 거리  y = 거친 노드의 갯수
    result[0][s] = 0

    heap = [(0, s, 0)]  # cost,현재 노드, 거친 노드 갯수
    while heap :
        cost,ky,depth = heappop(heap)

        flag = False
        # 이미 최소 거리가 있다면 굳이 정점을 더 거쳐가지 않아도 되므로
        # flag를 True로 바꿔준다
        for i in range(depth):
            if cost > result[ky][i] :
                flag = True
                break
        if flag or cost > result[ky][depth] :
            continue
        if depth + 1 <= N:
            for next_cost,next in G[ky] :
                prev = result[next][depth+1]
                new_cost = cost + next_cost
                if prev > new_cost :
                    result[next][depth+1] = new_cost
                    heappush(heap,(new_cost,next,depth+1))

    return result

N,M,K = map(int,input().split())
s,e = map(int,input().split())
G = [[] for _ in range(N+1)]
for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
    G[v2].append((cost,v1))

tlst = dijkstra()
for i in tlst :
    print(*i)
ret = [] # 이게 다익스트라로 구한 e까지 가는 모든 경로 리스트가 되야함

for i in range(N+1) :
    if tlst[e][i] != INF :
        ret.append([tlst[e][i],i])

dee = min(ret,key = lambda x:x[1])[1]
ans = min(ret)[0]
print(ans)
minD = 0
for _ in range(K) :
    p = int(input())
    if minD != dee :
        for a in ret :
            a[0] += p*(a[1])
        minD = min(ret)[1]
        ans = min(ret)[0]
        print(ans)
    elif minD == dee :
        ans += p*minD
        print(ans)


