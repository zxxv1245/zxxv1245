from heapq import heappop,heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
def dijkstra(k) :

    result = [[INF,0] for _ in range(N+1)]
    result[s][0] = 0
    heap = [(0,s,0)]

    while heap :
        cost, ky, dee = heappop(heap)

        if cost > result[ky][0] : continue

        for next_cost,next in G[ky] :
            prev = result[next][0]
            new_cost = cost + next_cost + k

            if prev > new_cost :
                result[next][0] = new_cost
                result[next][1] = dee+1

                heappush(heap,(result[next][0],next,result[next][1]))
    return result[e][0],result[e][1]

def dfs(x,k) :

    st = []
    visited = [0]*(N+1)
    st.append((x,0))
    visited[x] = 1

    while st :
        x,k = st.pop()
        if x == e :
            return k
        for cs,ky in G[x] :
            if visited[ky] != 1 :
                visited[ky] = 1
                st.append((ky,k+1))


N,M,K = map(int,input().split())
s,e = map(int,input().split())
G = [[] for _ in range(N+1)]
for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
    G[v2].append((cost,v1))
P = []

for _ in range(K) :
    p = int(input())
    P.append(p)
ret = []
minD = dfs(s,0)

ans,minDD = dijkstra(0)

print(ans)
i = 0
a = 0
while minD != minDD :
    a = P[i] + a
    ans,minDD = dijkstra(a)
    print(ans)
    i+=1
    if i >= K : break

while i < K :
    ans += P[i]*minD
    i += 1
    print(ans)


