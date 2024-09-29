import sys
import math

from collections import Counter




input = sys.stdin.readline
N = int(input().strip())
li = []

for i in range(N):
    li.append(int(input().strip()))
    
c = Counter(li)
max_c = max(c.values())

modes = [k for k,v in c.items() if v == max_c]
sorted_modes = sorted(modes)

one = round(sum(li)/len(li))

tmp = sorted(li)
two = tmp[len(tmp)//2]
if len(sorted_modes) == 1:
    
    three = sorted_modes[0]
else:
    three = sorted_modes[1]


four = tmp[-1] - tmp[0]

print(one)
print(two)
print(three)
print(four)


    
    
    