# score = list(range(5))

# index = 0
# while(index <= 4):
#     score[index] = int(input())
#     if score[index] < 40:
#         score[index] = 40
#     index += 1

# print( int(sum(score)/5) )

 #--------------------------------------------------

sum = 0 
for score in range(5):
    score = int(input())
    if score < 40:
        sum += 40
    else :
        sum += score
        
print(int(sum/5))


