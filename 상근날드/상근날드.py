# Hamburger = list(range(3))
# drink = list(range(2))

# index = 0
# for 


# index = 1

# for Hamburger in range(1, 4):
#     Hamburger[index] = int(input())
#     index += 1

# index = 1
# for drink in range(1, 3):
#     drink[index] = int(input())
#     index += 1

# print( min(Hamburger) + min(drink) - 50 )

hamburger = [int(input()) for _ in range(3)]
drink = [int(input()) for _ in range(2)]

print( min(hamburger) + min(drink) - 50 )

