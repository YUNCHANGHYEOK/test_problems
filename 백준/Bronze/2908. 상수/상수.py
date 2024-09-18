import sys
input = sys.stdin.readline


a,b = map(int,input().strip().split(' '))
#734


def sangsu(n):
    #7
    n1 = int(n / 100)

    #34
    n2 = int(n % 100)

    #3
    n3 = int(n2 / 10)

    #4
    n4 = int(n2 % 10)

    return (n4*100 + n3*10 + n1)

a1 = sangsu(a)
b1 = sangsu(b)

if(a1 > b1):
    print(a1)
else:
    print(b1)