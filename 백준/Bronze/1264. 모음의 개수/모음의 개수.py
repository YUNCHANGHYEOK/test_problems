import sys

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

for line in sys.stdin:
    line = line.strip()
    if line == "#":
        break
    print(sum(1 for char in line if char in vowels))
