n = int(input())
file_sizes = list(map(int, input().split()))
cluster_size = int(input())
total_space = 0

for size in file_sizes:
    if size == 0:
        continue
    total_space += ((size - 1) // cluster_size + 1) * cluster_size

print(total_space)
