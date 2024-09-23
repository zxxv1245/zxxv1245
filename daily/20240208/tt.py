def paper(A) :
    x = 1
    while True:

        if (A/10)%2 == 1 :
            x = x * 2 + 1
        elif (A/10)%2 == 0 :
            x = x * 2 - 1

        A = A + 10
        if A == N :
            return x

T = int(input())
for Test in range(1,T+1) :
    N = int(input())

    print(f'#{Test} {paper(10)}')