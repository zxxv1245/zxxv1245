# 시간 복잡도
# 실행 시간, 메모리 사용량

# Time complexty
# 기본 연산 수행 횟수 + 입력되는 data를 종합적으로 고려하여 계산하는 점근적 표기법

# 최선 표기법
# 평균 표기법
# **최악 표기법 = 코테 등등에서 선택해서 시간 복잡도를 계산함
## big O 표기법(최악 표기법 중 하나)

# a = 3
# b = 4
# c = 56
# print(a)
# print(b)
# n = int(input())
# for _ in range(n) :
# print("#")

n = int(input())
m = int(input())
for _ in range(n) :
    print('@')
for _ in range(m) :
    print('!')

for a in range(m) :
    for b in range(n) :
        print('#')