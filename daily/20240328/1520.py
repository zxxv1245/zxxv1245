# 1가지 경로에 대해서 깊이 우선 탐색 후 종점에 도착한다면 1을 리턴
# 리턴 받으며 해당 경로(값이 0인 곳을 통해서 돌아감)를 통해서 돌아갈 수 있는 경로를 재탐색한다고 생각
# (0,0)까지 돌아감, 종점에서 다른 경로가 있는지 재탐색
# 결국 0,0의 값이 N-1, M-1 에 갈 수 있는 값이 된다.
def dfs(i,j):

    if i == N-1 and j == M-1 :
        return 1
    if dp[i][j] == -1 : #내가 생각하지 못한 부분
        dp[i][j] = 0
        for a in range(4) :
            ni = i +di[a]
            nj = j +dj[a]
            if 0<=ni<N and 0<=nj<M and lst[i][j]>lst[ni][nj]:
                dp[i][j] += dfs(ni,nj)

    return dp[i][j]  # 내가 잘 이해하지 못했던 부분

N,M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)] #내가 생각하지 못한 부분 (-1로 시작한다는 걸 생각 못했음)
di,dj = [0,1,0,-1],[1,0,-1,0]

print(dfs(0,0))

