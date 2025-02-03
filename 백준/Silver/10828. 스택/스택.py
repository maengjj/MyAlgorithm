import sys

input=sys.stdin.readline

n = int(input())

stack = []
point = -1

for i in range(n):
    order = list(input().split())
    
    if order[0] == "push":
        order[1] = int(order[1])
        stack.append(order[1])
        point += 1
    elif order[0] == "pop":
        if point >= 0:
            print(stack[point])
            del stack[point]
            point -= 1
        else :
            print(-1)
    elif order[0] == "size":
        print((point+1))
    elif order[0] == "empty":
        if point == -1 :
            print(1)
        else :
            print(0)
    elif order[0] == "top":
        if point >= 0:
            print(stack[point])
        else :
            print(-1)