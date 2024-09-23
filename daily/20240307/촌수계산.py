def bfs(S) :

    visited[S] = 1
    Q = []
    Q.append(S)

    while Q :
        v = Q.pop()

        for w in G[v] :
            if visited[w] == 0 :
                visited[w] = visited[v]+1
                Q.append(w)



N = int(input())
S,F = map(int,input().split())
M = int(input())
G = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M) :
    v1,v2 = map(int,input().split())
    G[v1].append(v2)
    G[v2].append(v1)

bfs(S)

print(visited[F]-visited[S])
