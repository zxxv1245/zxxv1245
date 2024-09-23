
def dfs(k,cost,ds) :

    for next,next_cost in G[k] :
        if ds[next] == -1 :
            ds[next] = cost + next_cost
            dfs(next,ds[next],ds)




N = int(input())
G = [[]for _ in range(N+1)]
for _ in range(N-1) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((v2,cost))
    G[v2].append((v1,cost))



distance = [-1]*(N+1)
distance[0] = 0
distance[1] = 0
dfs(1,0,distance)

maxV = max(distance)
idx = distance.index(maxV)
distance1 = [-1]*(N+1)
distance1[0] = 0
distance1[idx] = 0
dfs(idx,0,distance1)

maxVx = max(distance1)
idxx = distance1.index(maxVx)
distance2 = [-1]*(N+1)
distance2[0] = 0
distance2[idxx] = 0
dfs(idxx,0,distance2)

for i in range(1,N+1) :
    print(max(distance1[i],distance2[i]))



for i in range(1,N+1) :

    distance = [-1]*(N+1)
    distance[0] = 0
    distance[i] = 0
    dfs(i,0,distance)

    maxV = max(distance)
    idx = distance.index(maxV)
    print(maxV,idx)