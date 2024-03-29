import math

# 절대값 알고리즘 1(부호 판단)
# 입력: 실수 a
# 출력: a의 절대값


def abs_sign(a: int):
    if a >= 0:
        return a
    else:
        return -a

# 절대값 알고리즘 2(제곱-제곱근)
# 입력: 실수 a
# 출력: a의 절대값


def abs_square(a: int):
    b = a * a
    return math.sqrt(b)  # 수학 모듈의 제곱근 함수


print(abs_sign(5))
print(abs_sign(-3))
print(abs_square(5))
print(abs_square(-3))
