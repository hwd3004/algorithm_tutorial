# 재귀 호출을 이용한 사각 나선 그리기

import turtle as t


def spiral(sp_len: int):
    if sp_len <= 5:
        return

    t.forward(sp_len)  # 앞으로 가기
    t.right(90)  # 오른쪽으로 90도 회전하기
    spiral(sp_len - 5)  # 재귀 호출으로 재귀 호출을 이용한 사각 나선 그리기


t.speed(0)  # 펜 속도를 0으로 설정하기 (속도를 빠르게 하면 그림이 느려짐). 범위는 0 ~ 10. 디폴트는 3.
spiral(200)  # 사각 나선 그리기 (200은 가장 큰 사각 나선의 길이). 범위는 50 ~ 200. 디폴트는 100.
t.hideturtle()  # 펜을 숨기기 (펜을 숨겨놓으면 사각 나선이 그려지지 않음)
t.done()  # 화면에 그린 그림을 확인하기 위해 종료
