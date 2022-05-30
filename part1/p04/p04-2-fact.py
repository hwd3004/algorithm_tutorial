def fact(n):
    if n <= 1:
        return 1
    
    # retun 10 * 9 * 8 * 7 ...
    return n * fact(n - 1)

# print(fact(1))
# print(fact(4))
# print(fact(5))
# print(fact(10))