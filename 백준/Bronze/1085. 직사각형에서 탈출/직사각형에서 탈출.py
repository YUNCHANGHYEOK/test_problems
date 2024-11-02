
x, y, w, h = map(int, input().split())

left = x
bottom = y
right = w - x
top = h - y

distance = min(left, bottom, right, top)

print(distance)
