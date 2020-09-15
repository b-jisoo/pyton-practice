score = list(range(5))

index = 0
while(index <= 4):
    score[index] = int(input())
    if score[index] < 40:
        score[index] = 40
    index += 1

print( int(sum(score)/5) )
