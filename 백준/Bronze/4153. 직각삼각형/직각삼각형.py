import math

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    sides = [a, b, c]
    max_side = max(sides)
    sides.remove(max_side)

    if max_side**2 == sides[0]**2 + sides[1]**2:
        print("right")
    else:
        print("wrong")