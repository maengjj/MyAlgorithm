N, M = map(int, input().split())
song = {}

for i in range(N):
    T, S, a1, a2, a3, a4, a5, a6, a7 = input().split()
    song[S] = [a1, a2, a3]

for i in range(M):
    B = input().split()
    cnt = 0
    title = ""

    for j in song:
        if B == song[j]:
            cnt += 1
            title = j

    if cnt >= 2:
        print("?")
    elif cnt == 1:
        print(title)
    else:
        print("!")
