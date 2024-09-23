from collections import deque

def bfs(i) :

    Q = deque()
    Q.append(i)
    visited[i] = 1

    while Q:
        v = Q.popleft()

        for w in G[v] :
            if visited[w] == 1 :
                continue
            visited[w] = 1
            Q.append(w)


N,M = map(int,input().split())
G = [[] for _ in range(N+1)]
ret = []
for _ in range(M) :
    v2,v1 = map(int,input().split())
    G[v1].append(v2)

maxV = -21e8
for i in range(1,N+1) :
    visited = [0]*(N+1)
    bfs(i)

    if maxV < visited.count(1) :
        maxV = visited.count(1)
        ret.clear()
        ret.append(i)
    elif maxV == visited.count(1) :
        ret.append(i)

print(*ret)
