# Add array elements

def sum(n, S):
    result = 0
    for i in range(1, n+1):
        result = result + S[i]
    return result


S = [-1, 10, 7, 11, 5, 13, 8]
res = sum(len(S)-1, S)
print(res)
