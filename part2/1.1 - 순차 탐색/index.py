# Sequential Search

def seqsearch(n, S, x):
    location = 1

    while(location <= n and S[location] != x):
        location += 1

    if(location > n):
        location = 0

    return location


S = [0, 10, 7, 11, 5, 13, 8]
x = 5
n = len(S)
res = seqsearch(n, S, x)
print(res)
