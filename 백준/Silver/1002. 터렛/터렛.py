T = int(input())

for _ in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 =  map(int, input().split())
    distance = ((x_1-x_2)**2 + (y_1-y_2) **2)**(1/2)            # 두점 사이의 거리를 distance라 하자. 그리고 각각의 점들과 거리를 기준으로 원을 그려보자.
    if distance == 0 and r_1 == r_2:                            # 두 점이 거리가 0(두 점이 똑같을 때), 그리고 반지름 길이가 똑같다면 두원은 같은 원이므로 류재명이 있을 수 있는 위치의 개수가 무한대
        print(-1)
    elif distance == (r_1+r_2) or distance == abs(r_1-r_2):     # 두원이 한 점에서 외접(거리=두원의 반지름의 합)하거나 내접(거리=두원의 반지름의 차)는 할때.
        print(1)
    elif distance <  (r_1+r_2) and distance > abs(r_1-r_2):     # 두 원이 두 점에서 만날때는 두 원의 반지름의차< 거리 < 두원의 반지름의 합
        print(2)
    else:                                                       # 나머지의 경우
        print(0)