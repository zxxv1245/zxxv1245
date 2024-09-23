import sys

T = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

M = max(A)
new_A = []
for a in A :
    new_a = a/M * 100
    new_A.append(new_a)

B = 0
for b in new_A :
    B += b
    avg = B/len(new_A)

print(avg)