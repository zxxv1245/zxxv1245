def is_prime_num(N) :
    arr = [1]*(2*N+1)
    arr[0] = 0
    arr[1] = 0

    for i in range(2,2*N+1) :
        if arr[i] == 1 :
            j = 2

        while i*j <= 2*N :
            if arr[i*j] == 1 :
                arr[i*j] = 0
            j+= 1
    return arr


while True :
    N = int(input())
    if N == 0 :
        break
    arr = is_prime_num(N)
    cnt = 0
    for i in range(N+1,2*N+1) :
        if arr[i] == 1 :
            cnt += 1
    print(cnt)
