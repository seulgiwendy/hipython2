#숫자 맞추기 게임에 이어, 숫자 야구 게임을 만들려고 합니다. 룰은 다음과 같습니다.

#컴퓨터는 0과 9 사이의 서로 다른 세 숫자를 임의의 순서로 뽑습니다. 사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추려고 합니다.
#컴퓨터는 사용자가 입력한 세 숫자에 대해서, 아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려줍니다.

#숫자의 값과 위치가 모두 일치하면 S입니다.
#숫자의 값은 일치하지만 위치가 틀렸으면 B입니다.
#예를 들어 컴퓨터가 1, 2, 3을 생성하였는데, 사용자가 1, 3, 5를 입력하면, 1S(1의 값과 위치가 일치) 1B(3의 값만 일치)입니다.
#기회는 무제한입니다. 하지만 몇번의 시도 끝에 맞췄는지 기록됩니다.
#3S(세 숫자의 값과 위치를 모두 맞춘 경우)일 때 게임이 끝납니다.
#진행 방식

#"0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다."가 출력됩니다.
#"세 수를 하나씩 차례대로 입력하세요."가 출력됩니다.
#"1번째 수를 입력하세요: "가 출력되고, 사용자로부터 입력을 받습니다. 마찬가지로 "2번째 수를 입력하세요: ", "3번째 수를 입력하세요: "가 출력되고, 사용자로부터 각각 입력을 받습니다. 만약 사용자가 중복되는 수를 입력하거나 범위에 벗어나는 수를 입력할 경우, 사용자로부터 입력을 다시 받습니다.
#사용자가 올바르게 서로 다른 세 수를 입력한 경우, 규칙에 따라 "*S *B"가 출력됩니다. 만약 3S가 아닌 경우 (2)번줄부터 다시 진행됩니다.
#사용자가 3S를 달성했을 때, "축하합니다. *번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다."가 출력됩니다.
#예시는 아래와 같습니다.
from random import randint

def computersball():
    computernumbers = []
    i = 0
    while len(computernumbers) < 3:
        new_number = randint(0, 9)

        # 새로운 수 나올때까지 다시 뽑기
        while new_number in computernumbers:
            new_number = randint(0, 9)
        computernumbers.append(new_number)

    print("0~9 사이의 랜덤한 숫자를 뽑았습니다.")
    return computernumbers


def usersball():
    usernumbers = []
    i = 0
    print("세 수를 하나씩 차례로 입력하세요.")
    while len(usernumbers) < 3:

        new_number = int(input("%d번째 숫자를 입력하시오." % (i + 1)))


        # 새로운 수 나올때까지 다시 뽑기
        while new_number in usernumbers:
            new_number = int(input("다른 숫자를 입력하시오."))
        usernumbers.append(new_number)
        while usernumbers [i] > 9:
            usernumbers [i] = int(input("범위에 맞는 숫자를 입력하시오."))
            if usernumbers [i] < 10:
                break

        #범위에 맞는 숫자 입력받기
        i = i + 1

    return usernumbers

def ballcheck(a, b):

    user_ball_array = []
    com_ball_array = []

    com_ball_array = a
    user_ball_array = b
    k = 0
    ball_count = 0

    while( k < len(a)):
        if ((user_ball_array[k] in com_ball_array) and not user_ball_array[k] == com_ball_array[k]):
            ball_count += 1

        k += 1

    return ball_count


def strikecheck(c, d):
    user_ball_array = []
    com_ball_array = []

    com_ball_array = c
    user_ball_array = d

    t = 0
    strike_count = 0

    while (t < len(c)):
        if (d[t] == c[t]):
            strike_count += 1

        t += 1
    return strike_count

guesses = []
numbers = []

numbers = computersball()
print(str(numbers))
guesses = usersball()


print(str(guesses))


i = 0
strike = 0
ball = 0
chance = 4
tries = 0

strike = strikecheck(numbers, guesses)
ball = ballcheck(numbers, guesses)



while (tries + 1 < chance):
    if (strike != 3):
        print("%dS %dB." % (strike, ball))
        guesses = usersball()
        strike = strikecheck(numbers, guesses)
        ball = ballcheck(numbers, guesses)


    else:
        print("축하합니다! %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (tries + 1))
        break
    tries += 1


if (tries == chance - 1) :
    if (strike == 3):
        print ("축하합니다! %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (tries + 1))
    else:
        print("기회 초과")




















