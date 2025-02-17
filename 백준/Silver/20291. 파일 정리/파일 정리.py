from collections import defaultdict
import sys
input = sys.stdin.readline
 
n = int(input())
dic = defaultdict(int)
 
for _ in range(n):
    file = input().rstrip().split('.')[1]
    dic[file] += 1
 
for i in sorted(dic.items()):
    print(' '.join(map(str, i)))