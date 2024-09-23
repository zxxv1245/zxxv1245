
def is_prime_num(M,N) :
    arr = [1]*(N+1)


    arr[0] = 0
    arr[1] = 0
    for i in range(M) :
        arr[i] = 0
    for i in range(2,N+1) :
            j = 2
            while (i*j) <=N :
                arr[i*j] = 0
                j+=1

    return arr
M,N = map(int,input().split())

arr = is_prime_num(M,N)

for a in range(len(arr)) :
    if arr[a] == 1:
        print(a)