A, B, C = map(int, input().split())

# 첫 번째 형태: A op B = C
if A + B == C:
    print(f"{A}+{B}={C}")
elif A - B == C:
    print(f"{A}-{B}={C}")
elif A * B == C:
    print(f"{A}*{B}={C}")
elif B != 0 and A // B == C and A % B == 0:
    print(f"{A}/{B}={C}")

# 두 번째 형태: A = B op C
elif B + C == A:
    print(f"{A}={B}+{C}")
elif B - C == A:
    print(f"{A}={B}-{C}")
elif B * C == A:
    print(f"{A}={B}*{C}")
elif C != 0 and B // C == A and B % C == 0:
    print(f"{A}={B}/{C}")
