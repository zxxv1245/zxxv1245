# 파이참 디버깅 단축키 입니다.
#
# Ctrl + F8 : Toggle breakpoint
# shift + f9 : 디버깅 시작
# Ctrl + F2 : 디버깅 종료
# F8 : Step over
# F7 : Step into
# F9 : resume (다음 break point까지 실행)


def sum(y,x):
    z=y+x
    z+=1
    return z
a=10
b=20
b=30
b=40
b=50
b=60

ret=sum(a,b)
print(ret)