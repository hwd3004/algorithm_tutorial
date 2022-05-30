# 1에서 n까지 숫자들의 제곱의 합

def a(n):
    s = 0
    
    return (n * (n + 1) * (2 * n + 1)) // 6

print(a(10))