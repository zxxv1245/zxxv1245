T =  input()
alpha_list =['c=','c-','dz=','d-','lj','nj','s=','z=']

for a in alpha_list :
    if a in T :
        T = T.replace(a, 'a')

T = T.upper()
for b in T :
    if 'A' <= b <= 'Z' :
        T = T.replace(b, 'A')

print(T.count('A'))