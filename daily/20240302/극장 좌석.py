
N = int(input())
M = int(input())

lst = list(range(0,N+1))
arr = []
for _ in range(M) :
    a = int(input())
    arr.append(a)


dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1
for i in arr :
    dp[i] = 1
    if i + 1 <= N:
        dp[i+1] = 1

ret = []
for i in range(2,N+1) :
    if dp[i] == 0 :
        dp[i] = dp[i-1] + dp[i-2]
    elif dp[i] != 0 :
        ret.append(dp[i-1])

ret.append(dp[-1])
ans = ret[0]
ret.pop(0)
for a in ret :
    ans *= a

print(ans)