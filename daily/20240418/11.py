a,b,c = map(int,input().split())
n = int(input())
c += n%60
n = n//60
if c >= 60 :
    c -= 60
    b += 1

b += n%60
n = n//60
if b >= 60 :
    b -= 60
    a += 1

a += n % 24
if a >= 24 :
    a -= 24

print(a, b, c)