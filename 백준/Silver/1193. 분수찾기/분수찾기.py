X = int(input())
New_X = X
line= 1

# X에서 1부터 1씩 증가시킨 값을 빼준다. X가 빼주는 값보다 작아지는 경우 멈춘다.
# 그 순간 빼려는 값이 몇번째 라인인지 보여주는 값이다.
while New_X > line:
    New_X -= line
    line += 1

array_list = list(range(int(line*(line-1)/2 + 1), int((line+1)*line/2)+1))

if line % 2 == 0:       # 짝수라인이라면
    print(int(array_list.index(X))+1, '/',  int(line-array_list.index(X)) , sep='')
else:                   # 홀수라인이라면
    print(int(line-array_list.index(X)), '/', (array_list.index(X))+1, sep='')