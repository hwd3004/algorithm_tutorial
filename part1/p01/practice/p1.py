# 1에서 n까지 숫자들의 제곱의 합

def a(n):
    s = 0
    
    for i in range(1, n + 1):
        s = s + (i * i)
        
    return s

print(a(10))