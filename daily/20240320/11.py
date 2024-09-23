# bfs ?
# visited 배열 필요
# 인접 리스트
from collections import deque


def bfs(S):
    Q = deque()
    Q.append((S, 1))
    visited = [0] * 101
    visited[S] = 1
    ret = []
    while Q:
        x, cnt = Q.popleft()
        ret.append((x, cnt))

        for w in G[x]:
            if visited[w] == 0:
                visited[w] = 1
                Q.append((w, cnt + 1))
    return ret


T = 10
for Test in range(1, T + 1):
    M, S = map(int, input().split())
    lst = list(map(int, input().split()))
    G = [[] for _ in range(101)]

    for i in range(0, M, 2):
        v1, v2 = lst[i], lst[i + 1]
        G[v1].append(v2)

    result = bfs(S)
    result.sort()
    result.sort(key=lambda x: x[1])

    print(f'#{Test} {result[-1][0]}')