import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(s,cost) :
    for next,next_cost in G[s] :
        if distance[next] == -1 :
            new_cost = cost + next_cost
            distance[next] = new_cost
            dfs(next,new_cost)
        elif distance[next] >= cost + next_cost :
            distance[next] = cost + next_cost
            dfs(next,cost + next_cost)
    print(distance)

    return max(distance)

N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((v2,cost))
    G[v2].append((v1,cost))


distance = [-1] * (N + 1)
distance[0] = 0
for i in range(1,N+1) :
    distance[i] = 0
    ans=dfs(i,0)
    distance[i] = -1
    print(ans)