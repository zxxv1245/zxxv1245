N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

for i in range(N) :
    for j in range(N) :
        if i-1 < 0 and j-1 < 0:
            continue       # 0,0 넘어가기

        elif i-1 < 0 :      # x 가 0 일땐 왼쪽만 보기
            if lst[i][j] < lst[i][j-1] :
                dp[i][j] = dp[i][j-1]
            else :
                dp[i][j] = dp[i][j-1] + (lst[i][j] - lst[i][j-1] + 1)
        elif j-1 < 0 :      # y가 0 일땐 위만 보기
            if lst[i][j] < lst[i-1][j]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + (lst[i][j] - lst[i-1][j] + 1)
        else :            # 둘 다 0이 아닐땐? 위, 왼쪽 둘 다 보기
            if lst[i][j] < lst[i][j - 1]:
                pre_i = dp[i][j - 1]
            else:
                pre_i = dp[i][j - 1] + (lst[i][j] - lst[i][j - 1] + 1)
            if lst[i][j] < lst[i-1][j]:
                pre_j = dp[i-1][j]
            else:
                pre_j = dp[i-1][j] + (lst[i][j] - lst[i-1][j] + 1)

            dp[i][j] = min(pre_i,pre_j)

print(dp[N-1][N-1])