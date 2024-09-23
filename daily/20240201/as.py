import sys

sys.stdin = open('input.txt', 'r')


T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int, input().split()))
    M = N//2
    for x in range(N-1) :
        minP = x
        for y in range(x+1, N) :
            if lst[minP] > lst[y] :
                minP = y
        lst[x], lst[minP] = lst[minP], lst[x]

    new_lst = lst[M:]
    lst = lst[:M]


    for i in range(M-1) :
        maxV = -21e8
        maxP = 0
        for j in range(i, M) :
            if maxV < new_lst[j] :
                maxV = new_lst[j]
                maxP = j
        new_lst[i], new_lst[maxP] = new_lst[maxP], new_lst[i]

    for a in range(0,N,2) :
        lst.insert(a, new_lst[a//2])

    print(f'#{Test}', *lst[:10])