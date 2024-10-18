a = list(input())

if len(a) == 2:
    print(int(a[0]) + int(a[1]))
elif len(a) == 3:
    # 중간에 0이 있는 경우 (예: 110)
    if a[1] == '0':
        print(int(a[0]) * 10 + int(a[2]))
    else:
        print(int(a[0]) + int(a[1] + a[2]))
elif len(a) == 4:
    print(int(a[0] + a[1]) + int(a[2] + a[3]))
