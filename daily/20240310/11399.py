N = int(input())

lst = sorted(list(map(int,input().split())))
ret = 0

for i in range(N+1) :
    for j in range(i) :
        ret += lst[j]

print(ret)