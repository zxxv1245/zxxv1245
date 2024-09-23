from heapq import heappop, heappush
import sys
INF = float('inf')
input = sys.stdin.readline
def dfs(x, k, sumV, visited, ret, G):
    global mind,minD
    if k > minD:
        return
    if x == e:
        if mind > k:
            mind = k
        ret.append([sumV, k])
        return

    for cost, ky in G[x]:
        if not visited[ky]:
            visited[ky] = True
            dfs(ky, k + 1, sumV + cost, visited, ret, G)
            visited[ky] = False

def dijkstra(N, s, e, G):
    result = [[INF, 0] for _ in range(N + 1)]
    result[s][0] = 0

    heap = [(0, s, 0)]
    while heap:
        cost, ky, dee = heappop(heap)

        if cost > result[ky][0]:
            continue

        for next_cost, next_node in G[ky]:
            prev = result[next_node][0]
            new_cost = cost + next_cost

            if prev > new_cost:
                result[next_node][0] = new_cost
                result[next_node][1] = dee + 1
                heappush(heap, (new_cost, next_node, result[next_node][1]))

    return result[e][1]

N, M, K = map(int, input().split())
s, e = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2, cost = map(int, input().split())
    G[v1].append((cost, v2))
    G[v2].append((cost, v1))

minD = dijkstra(N, s, e, G)
mind = INF
visited = [False] * (N + 1)
visited[s] = True
ret = []
dfs(s, 0, 0, visited, ret, G)
dee = min(ret)[1]
ans = min(ret)[0]
print(ans)

for _ in range(K):
    p = int(input())
    if mind != dee:
        for a in ret:
            a[0] += p * a[1]
        dee = min(ret)[1]
        ans = min(ret)[0]
        print(ans)
    elif mind == dee:
        ans += p * dee
        print(ans)
