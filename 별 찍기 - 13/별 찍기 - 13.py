# num = int(input())
# star = []
# for num in range(1, num + 1):
#     star.append("*")
#     print(star)
    
    
# num = int(input())
# star = []
# i = 0
# while(i < num ):
#     star.append("*")
#     print(star)
#     i += 1
#     if(i == num):
#         while (num > 1):
#             star.pop()
#             print(star)
#             num -= 1
#         break


# num = int(input())
# star = []
# for _ in range(num):
#     star.append("*")
#     print(star)
# for _ in range(num-1):
#     star.pop()
#     print(star)

num = int(input())
i = 1
while(i < num ):
    print("*"*i)
    i += 1
while(i >= 1):
    print("*"*i)
    i -= 1


