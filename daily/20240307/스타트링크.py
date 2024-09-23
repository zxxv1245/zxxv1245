def bfs(S) :
    global U
    global D
    global G
    global F
    Q = deque()
    Q.append(S)
    visited[S] = 1
    visited[0] = 1
    while Q :
        v = Q.popleft()
        if v == G :
            return visited[v] -1
        v1 = v+U
        v2 = v-D
        if v1 < F+1 and visited[v1] == 0 :
            Q.append(v1)
            visited[v1] = visited[v] +1
        if 0<v2  and visited[v2] == 0 :
            Q.append(v2)
            visited[v2] = visited[v] +1
    return 'use the stairs'


from collections import deque

F,S,G,U,D = map(int,input().split())
visited = [0]*1000001

print(bfs(S))



