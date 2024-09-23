T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    info = [[] for _ in range(N)]
    for i in range(N):
        info[i] = list(map(int, input().split()))

    result = 0
    for i1 in range(N - 1):
        for i2 in range(i1 + 1, N):
            l1, r1 = info[i1]
            l2, r2 = info[i2]
            # 한 끝점은 A가 더 높고 다른 한 끝점은 B가 더 높은 경우 -> 교차 
            if ((l1 > l2 and r1 < r2) or
                    (l1 < l2 and r1 > r2)):
                result += 1

    print(f'#{tc} {result}')