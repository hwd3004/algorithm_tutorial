# 최대공약수

def gcd(a:int, b:int):
    n = min(a, b)
    r = 1
    
    for i in range(n, 1, -1):
        if a % i == 0 and b % i == 0:
            r = i
            break;
            
    return r

print(gcd(1, 5))
print(gcd(4, 6))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))