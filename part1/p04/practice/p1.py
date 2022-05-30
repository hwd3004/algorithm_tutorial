def sum_n(n):
    s = 0
    
    # for i in range(1, n + 1):
    #     s = s + i
        
    # return s
    if n <= 1:
        return 1
    
    return n + sum_n(n - 1)

print(sum_n(10))