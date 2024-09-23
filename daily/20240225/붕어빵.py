T = int(input())

for Test in range(1,T+1) :
    N,M,K = map(int,input().split())
    person = list(map(int,input().split()))
    MaxV = max(person)
    a = M
    ret = 'Possible'
    bung = 0
    for time in range(MaxV+1) :
        if time == M :
            bung += K
            M += a
        for j in range(N) :
            if time == person[j] :
                bung -= 1
                if bung < 0 :
                    ret = 'Impossible'
        if ret == 'Impossible' :
            break

    print(f'#{Test} {ret}')