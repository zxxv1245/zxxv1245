def dfs(s) :
    stack = []
    visited = [0] * 100
    stack.append(s)
    visited[s] = 1

    while stack :
        value = stack.pop()

        for w in G[value] :
            if w == 99 :
                return 1
            if visited[w] == 0 :
                stack.append(w)
                visited[w] = 1
    return 0


T = 10
for _ in range(1,T+1) :
    TC, N = map(int,input().split())
    lst = list(map(int, input().split()))
    G = [[]for _ in range(100)]
    N = N*2

    for i in range(0, N, 2) :
        v1 = lst[i]
        v2 = lst[i+1]
        G[v1].append(v2)

    print(f'#{TC} {dfs(0)}')