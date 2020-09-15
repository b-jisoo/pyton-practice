num = int(input())
temp = num
i = 0
while(1 < num ):
    print(" "*i + "*" + "*"*(num - 1) * 2)
    num -= 1
    i += 1


while(temp >= num):
    print(" "*i + "*" + "*"*(num - 1) * 2)
    num += 1
    i -= 1




