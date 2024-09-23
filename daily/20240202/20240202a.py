T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    count_lst = [0]*5001
    for i in range(N) :
        A, B = map(int,input().split())

        for x in range(A,B+1) :
            count_lst[x] += 1


    P = int(input())
    C_lst = [int(input()) for _ in range(P)]
    print(f'#{Test}', end = ' ')
    for i in C_lst :
        print(count_lst[i], end = ' ')
    print()