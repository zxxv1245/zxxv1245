N = int(input())

for i in range(N) :
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A = A[1:]
    B = B[1:]
    A.sort(reverse=True)
    B.sort(reverse=True)

    while True :
        if A :
            va = A.pop(0)
        else :
            va = 0

        if B :
            vb = B.pop(0)
        else :
            vb = 0

        if va > vb :
            print('A')
            break
        elif va < vb :
            print('B')
            break

        if not A and not B :
            print('D')
            break

