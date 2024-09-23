N,L,I = map(int,input().split())
cnt = 0
for i in range(2**N) :
    if bin(i)[2:].count('1') == L :
        cnt += 1
    if cnt == I :
        print(bin(i)[2:])


