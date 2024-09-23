start = int(input())
N = int(input())

lst = [list(input().split()) for _ in range(N)]

cnt = 0
q = 0
ret = start
while q < N :
    cnt += int(lst[q][0])
    if cnt >= 210 :
        break
    if lst[q][1] == 'T' :
        ret += 1
        if ret == 9 :
            ret = 1
    q += 1
print(ret)
