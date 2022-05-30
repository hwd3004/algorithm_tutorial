def find_max_indx(a):
    n = len(a)
    max_v = a[0]
    indx = 0
    
    for i in range(1, n):
        
        if a[i] > max_v:
            indx = i
            max_v = a[i]
    
    return indx

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_max_indx(v))