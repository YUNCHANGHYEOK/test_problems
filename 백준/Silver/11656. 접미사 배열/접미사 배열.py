#10773
import sys
input = sys.stdin.readline

a = input().strip()
li = []
for i in range(len(a)):
    slicing = a[i:]
    li.append(slicing)

li = sorted(li)
for i in range(len(li)):
    print(li[i])

    