def is_prime_number(N,K) :
    arr = [1]*(N+1)

    arr[0] = 0
    arr[1] = 0
    cnt = 0
    for i in range(2,N+1) :
        if arr[i] == 1 :
            j = 1

            while i*j <= N :
                if arr[i*j] == 1 :
                    arr[i*j] = 0
                    cnt += 1
                if cnt == K :
                    return i*j
                j += 1
N,K = map(int,input().split())

arr = is_prime_number(N,K)

print(arr)