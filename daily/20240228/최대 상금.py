def abc(k,lst):
    global maxV

    if k == N:
        ret = ''
        for i in lst:
            ret += i
        maxV = max(maxV,int(ret))
        return

    for i in range(M - 1):
        for j in range(i + 1, M):
            lst[i], lst[j] = lst[j], lst[i]
            abc(k + 1,lst)



T = int(input())

for Test in range(1, T + 1):
    A, N = map(int, input().split())
    lst = []
    for i in str(A):
        lst.append(i)
    M = len(lst)
    maxV = -21e8
    k = 0
    used = []
    temp = lst[:]
    temp.append(k)
    abc(k,lst)
    print(f'#{Test} {maxV}')