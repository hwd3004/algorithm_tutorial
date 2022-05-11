# https://play.google.com/books/reader?id=LusoDwAAQBAJ&pg=GBS.PT58.w.3.0.5_43&hl=ko&num=19&printsec=frontcover

# 동명이인을 찾는 알고리즘

arr1 = ["Tom", "Jerry", "Mike", "Tom"]
arr2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]


def func(arr: list[str]):
    s = set()

    for i in range(len(arr)):

        target: str = arr[i]

        for j in range(i + 1, len(arr)):
            # print(f"{target} == {arr[j]}")

            if(target == arr[j]):
                s.add(target)

    print(s)


func(arr1)
func(arr2)


def find_same_name(a):
    n = len(a)

    result = set()

    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])

    print(result)


find_same_name(arr1)
find_same_name(arr2)
