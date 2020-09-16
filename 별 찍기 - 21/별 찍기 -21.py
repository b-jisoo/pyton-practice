

i = int(input())
for j in range(1, i + 1):
    print("*" + " *" * int(((i + 1) / 2) - 1))
    if i == 1:
        continue
    print(" *"* int(i / 2) )

