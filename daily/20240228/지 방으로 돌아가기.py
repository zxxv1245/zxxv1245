T = int(input())

for Test in range(1, T + 1):
    N = int(input())
    start = 0
    end = 0
    cnt = 1

    for _ in range(N):
        A, B = map(int, input().split())
        if A>B :
            A,B = B,A
        if end >= A:
            cnt += 1
            start = B
        else:
            start = A
            end = B

    print(f'#{Test} {cnt}')