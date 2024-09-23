N = int(input())
cnt = 0
while N != 1:

    if (N-1) % 3 == 0  :
        N -= 1
        N /= 3
        cnt += 2
    elif N % 3 == 0 :
        N = N/3
        cnt += 1
    elif (N-1) % 2 == 0 :
        N -= 1
        N /= 2
        cnt += 2

    elif N % 2 == 0 :
        N = N/2
        cnt += 1

print(cnt)