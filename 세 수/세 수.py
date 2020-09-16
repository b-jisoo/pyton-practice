# A, B, C = map(int, input().split())


# if (A>=B and A<=C) or (A>=C and A<=B):
#     print(A)
# elif (B>=A and B<=C) or (B>=C and B<=A):
#     print(B)
# else:
#     print(C)
 #--------------------------------------------------

A, B, C = map(int, input().split())

if C <= A <= B or B <= A <= C :
    print(A)
elif C <= B <= A or A<= B <= C :
    print(B)
else:
    print(C)