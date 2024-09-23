N = int(input())

if N == 1 :
    print(666)
else :
    cnt = 1
    for i in range(1666, 100000000) :
        if '666' in str(i) :
            cnt += 1

        if cnt == N :
            print(i)
            break
