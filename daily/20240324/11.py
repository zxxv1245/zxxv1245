def decTobin(num) :
    s = ''
    for j in range(3,-1,-1) :
        if num & 1 << j :   # s+= '1' if num & 1 << j esls '0'
            s += '1'
        else :
            s += '0'
    return s

def bitprint(num) :
    for j in range(3,-1,-1) :
        if num & 1 << j :
            print(1)
        else :
            print(0)

# 16진수 값 하나를 이진수 4자의 문자열로 변환
def hexTobin(hexC) :
    decV = int(hexC, 16)
    a = decTobin(decV)
    return a

num = 7

print(hexTobin('7'))
print(hexTobin('F'))

print(decTobin(num))
bitprint(7)
print(bin(7))


