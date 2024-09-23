# 배운 점
# 1. 분할 정복을 이용한 거듭제곱
# 2. 수가 엄청나게 커지면 그것 역시 연산 속도에 큰 차이를 준다(미리 연산할 수 있으면 미리 연산할 것)

import sys
input = sys.stdin.readline
A,B,C = map(int,input().split())

# python 내장함수
# ret = pow(A,B,C)
# print(ret)

# 반복문 이용
# def pw(k,n,c) :
#     ret = 1
#     while n :
#         if n % 2 == 1 :
#             ret = (ret*k)%c
#         k = (k*k)%c
#         n //= 2
#     return  ret



#재귀
# def pw(k,n,c) :
#     if n == 0 :
#         return 1
#     else :
#         x = pw(k,n//2,c)
#         if n % 2 == 0 :
#             return (x*x)%c
#         else :
#             return (x*x*k)%c


# 비트연산자 & 반복문
def pw(k,n,c) :
    ret = 1
    while n :
        if n&1 :
            ret = (ret*k)%c
        k = (k*k)%c
        n = n>>1
    return ret

print(pw(A, B, C))
