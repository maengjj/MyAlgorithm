N, M = map(int, input().split())
students = []
cnt = {}
ans = 0

for i in range(N):
    student_num = int(input())
    students += input().split()

for student in students:
    if student in cnt:
        cnt[student] += 1
    else:
        cnt[student] = 1

for num in cnt.values():
    if num >= M:
        ans += 1

print(ans)