E,S,M = map(int,input().split())

# 1<= E <=15   1<=S<=28   1 <= M <= 19

e = 0
s = 0
m = 0
i = 0
while True :
    i += 1

    e = i % 15
    if e == 0 :
        e = 15
    s = i % 28
    if s == 0 :
        s = 28
    m = i % 19
    if m == 0 :
        m = 19
    if E == e and S == s and M == m :
        break
print(i)