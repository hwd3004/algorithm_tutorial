def func(arr: list[str]):
    s = set()

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            # print(f"{arr[i]} - {arr[j]}")
            s.add(f"{arr[i]} - {arr[j]}")

    print(s)
    
arr1 = ["Tom", "Jerry", "Mike"]

func(arr1)
