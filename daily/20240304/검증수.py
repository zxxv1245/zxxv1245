lst = list(map(int,input().split()))

ret = 0
for i in lst :
    ret += i**2

ret %= 10

print(ret)

