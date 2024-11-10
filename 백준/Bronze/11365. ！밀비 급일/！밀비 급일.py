import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == "END":
        break
    print(line[::-1])
