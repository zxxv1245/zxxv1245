def bfs(s) :
    global N
    global cnt
    visited = [0]*(N+1)
    visited[s] = 1
    Q = []
    Q.append(s)

    while Q :
        v = Q.pop()

        for w in G[v] :
            if visited[w] == 0 :
                Q.append(w)
                visited[w] = 1
                cnt += 1

N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]
for _ in range(M) :
    v1,v2 = map(int,input().split())
    G[v1].append(v2)
    G[v2].append(v1)
cnt = 0
bfs(1)

print(cnt)