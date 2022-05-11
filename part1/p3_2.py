# https://play.google.com/books/reader?id=LusoDwAAQBAJ&pg=GBS.PT64.w.3.0.5_38&hl=ko&num=19&printsec=frontcover

arr1 = ["Tom", "Jerry", "Mike"]


def func(arr: list[str]):
    s = set()

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            # print(f"{arr[i]} - {arr[j]}")
            s.add(f"{arr[i]} - {arr[j]}")

    print(s)

func(arr1)
