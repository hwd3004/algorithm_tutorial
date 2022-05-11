# https://play.google.com/books/reader?id=LusoDwAAQBAJ&pg=GBS.PT69&hl=ko&num=19&printsec=frontcover

def factorial(n: int):
    result = 1
    for i in range(1, n+1):
        result = result * i

    print(result)


factorial(3)
factorial(4)
factorial(5)
factorial(10)


def fact(n: int):
    if n <= 1:
        return 1

    return n * fact(n-1)


print(fact(3))
print(fact(4))
print(fact(5))
