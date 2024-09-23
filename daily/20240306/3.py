# 연습문제 3번
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# 최대 깊이 7
def dfs(S,N) :
    visited = [0]*(N+1)
    st = []
    visited[S] = 1
    print(S)
    while True :
        for w in G[S] :
            if visited[w] == 0 :
                st.append(S)
                S = w
                visited[S] = 1
                print(S)
                break
        else :
            if st :
                S = st.pop()
            else :
                break
N = 7
lst = list(map(int,input().split()))

G = [[] for _ in range(N+1)]

for i in range(0,len(lst)-1,2) :
    n1 = lst[i]
    n2 = lst[i+1]
    G[n1].append(n2)
    G[n2].append(n1)

print(G)
dfs(1,N)