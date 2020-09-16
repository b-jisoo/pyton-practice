A, B, C = sorted(list(map(int, input().split())))


# print(A)
# print(B)
# print(C)

if B <= A <= C:
    print(A)
elif A <= B <= C:
    print(B)
else:
    print(C)

