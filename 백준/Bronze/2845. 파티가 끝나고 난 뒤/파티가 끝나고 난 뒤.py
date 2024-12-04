
L, P = map(int, input().split())
reported = list(map(int, input().split()))

actual = L * P

result = [x - actual for x in reported]
print(" ".join(map(str, result)))
