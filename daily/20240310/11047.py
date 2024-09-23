N,K = map(int,input().split())

lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)

i = 0
cnt = 0
while K >0 :
    if K >= lst[i] :
        K -= lst[i]
        cnt +=1
    else :
        i += 1

print(cnt)