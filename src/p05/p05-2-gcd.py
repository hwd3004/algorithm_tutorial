# 유클리드 알고리즘
#
# • a와 b의 최대공약수는 ‘b’와 ‘a를 b로 나눈 나머지’의 최대공약수와 같습니다. 즉, gcd(a, b) = gcd(b, a % b)입니다.
# • 어떤 수와 0의 최대공약수는 자기 자신입니다. 즉, gcd(n, 0) = n입니다.
#
# gcd(60, 24) = gcd(24, 60 % 24) = gcd(24, 12) = gcd(12, 24 % 12) = gcd(12, 0) = 12
# gcd(81, 27) = gcd(27, 81 % 27) = gcd(27, 0) = 27

# 최대공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수

def gcd(a: int, b: int):
    if b == 0:  # 종료 조건
        return a

    return gcd(b, a % b)  # 좀 더 작은 값으로 자기 자신을 호출


print(gcd(60, 24))
print(gcd(81, 27))
