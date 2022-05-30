def find_same_name(arr):
    set1 = set()
    
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            # print(f"{arr[i]} == {arr[j]}")
            if arr[i] == arr[j]:
                set1.add(arr[i])
            
    print(set1)


name = ["Tom", "Jerry", "Mike", "Tom"]
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]

find_same_name(name)
find_same_name(name2)