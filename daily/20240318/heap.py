def abc(root):
    global last
    last += 1  # 마지막 노드 추가(완전이진트리 유지)
    arr[last] = root  # 마지막 노드에 데이터 삽입
    c = last  # 부모 < 자식
    p = c // 2  # 부모번호 계산
    while p >= 1 and arr[p] > arr[c]:
        arr[p], arr[c] = arr[c], arr[p]
        c = p
        p = c // 2


T = int(input())
for Test in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    arr = [0] * (N + 1)
    last = 0

    for a in lst:
        abc(a)

    ret = 0
    while N > 0:
        ret += arr[N // 2]
        N = N // 2
    print(f'#{Test} {ret}')