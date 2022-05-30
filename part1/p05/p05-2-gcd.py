# 최대공약수를 유클리드 알고리즘을 이용해 구하기
# a와 b의 최대공약수는 b와, a를 b로 나눈 나머지의 최대공약수와 같다
# gcd(a, b) = gcd(b, a % b)

# gcd(60, 24) = gcd(24, 60 % 24)
# = gcd(24, 12) = gcd(12, 24 % 12)
# = gcd(12, 0) = 12

def gcd(a:int, b:int):
    if a % b == 0:
        return b
    
    return gcd(b, a % b)

print(gcd(1, 5))
print(gcd(4, 6))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))