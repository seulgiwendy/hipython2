from random import randint

random_integer = randint(1, 20)
answer = 0
chance = 0

print (random_integer)
while (chance <= 4):
    if (chance == 4):
        print("아쉽습니다. 정답은 %d 입니다." % (random_integer))
        break


    answer = int(input("기회가 %d번 남았습니다. 1~20 사이의 숫자를 맞춰보세요:" % (4-chance)))
    if (answer == random_integer):
        print ("축하합니다. %d번만에 숫자를 맞추셨습니다." % (chance+1))
        break

    elif (answer > random_integer):
        print ("Down")

    elif (answer < random_integer):
        print ("Up")
    chance = chance + 1


