Data = [0,4,1,3,1,2,4,1]

N = 4
K = 8
counts = [0] * (N+1)
temp = [0,0,0,0,0,0,0,0]


for a in Data :
    counts[a] += 1

for r in range(1,N+1) :
    counts[r] = counts[r] + counts[r-1]

for i in range(K-1, -1,-1) :
    counts[Data[i]] -= 1
    temp[counts[Data[i]]] = Data[i]
print(temp)