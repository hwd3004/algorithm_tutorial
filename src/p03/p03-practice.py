# n명 중 두 명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘을 만들기
# 예를 들어 입력이 리스트 ["Tom", "Jerry", "Mike"]라면 다음과 같은 세 가지 경우를 출력
# Tom - Jerry, Tom - Mike, Jerry - Mike

def main(arr: list[str]):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(arr[i], '-', arr[j])


main(['Tom', 'Jerry', 'Mike'])
