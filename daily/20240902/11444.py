n = int(input())
dp = {}

def fb(n) :
    if n in dp :
        return dp[n]
    if n == 0 :
        return 0
    if n == 1 or n == 2:
        return 1
    if n % 2 == 1 :
        dp[n//2 + 1] = fb(n//2 + 1)%1000000007
        dp[n//2] = fb(n//2)%1000000007
        return dp[n//2 + 1] ** 2 + dp[n // 2] ** 2
    else :
        dp[n // 2 + 1] = fb(n // 2 + 1) % 1000000007
        dp[n // 2 - 1] = fb(n // 2 - 1) % 1000000007
        return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2


print(fb(n)%1000000007)