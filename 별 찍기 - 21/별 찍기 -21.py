# i = int(input())

# while(i >= 0):
#     if ( i % 2) == 1 :
#         print("*")
#     if ( i % 2) == 0 :
#         print(" " * (i - 1) + "*" * (i - 1))
#     i -= 1

# i = int(input())

# while(i > 0):   
#     print("*")
#     print(" " * ((i - 1) % 2) + "*" * ((i - 1) % 2))
#     i -= 1

i = int(input())
for j in range(1, i + 1):
    print("*" + " *" * int(((i + 1) / 2) - 1))
    if i == 1:
        continue
    print(" *"* int(i / 2) )

