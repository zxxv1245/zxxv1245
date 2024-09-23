N,K = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
lst.sort(key = lambda x:x[1],reverse=True)
# 0 무게 1 가격
arr = [int(input()) for _ in range(K)]
ret = 0

j = 0
for i in range(K) :
    ba = arr[i]
    pre = 0
    while True :
        if lst[j][0] <= ba :
            pre += lst[j][1]
            ba -= lst[j][0]
        j+=1
    ret += pre

print(ret)