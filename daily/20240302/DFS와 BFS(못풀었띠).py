def dfs(S):
    st = []
    visited = [0]*(N+1)

    st.append(S)

    visited[S] = 1
    while st :
        v = st.pop()




N,M,S = map(int,input().split())
G = []
for _ in range(M) :
    v1,v2 = map(int,input().split())
    G.append((v1,v2))

dfs(S)