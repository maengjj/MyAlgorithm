N = int(input())
recipe = input().split()
use = input().split()

for i in recipe:
    if i not in use:
        print(i)