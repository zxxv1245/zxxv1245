N = int(input())
st = []

for _ in range(N) :
    a = int(input())
    if a != 0 :
        st.append(a)
    else :
        st.pop()

print(sum(st))