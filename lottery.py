from random import randint

# 무작위로 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    # 코드를 입력하세요
    computernumbers = []
    i = 0
    while len(computernumbers) < 6:
        new_number = randint(1, 45)

        # 새로운 수 나올때까지 다시 뽑기
        while new_number in computernumbers:
            new_number = randint(1, 45)
        computernumbers.append(new_number)
    computernumbers = sorted(computernumbers)
    return computernumbers

# 보너스까지 포함해 7개 숫자 뽑기
def draw_winning_numbers():
    number_row = []
    input_row = generate_numbers()
    bonus_number = randint(1, 45)
    while bonus_number in input_row:
        bonus_number = randint(1, 45)
    input_row.append(bonus_number)
    number_row = input_row
    return number_row

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):

    i = 0
    count = 0

    while (i<len(list2)-1):
        if list2[i] in list1:
            count += 1
        i += 1
    return count




# 로또 등수 확인하기
def check(numbers, winning_numbers):
    prize_count = count_matching_numbers(numbers, winning_numbers)
    bonus_digit = winning_numbers[6]
    prize_money = 0
    if prize_count == 6:
        prize_money = 1000000000

    elif prize_count == 5 and bonus_digit in numbers:
        prize_money = 50000000

    elif prize_count == 5:
        prize_money = 1000000
    elif prize_count == 4:
        prize_money = 50000
    elif prize_count == 3:
        prize_money = 5000
    return prize_money


auto = generate_numbers()
print(auto)

chucheom = draw_winning_numbers()
print(chucheom)
dangcheomgeum = check(auto, chucheom)

print(dangcheomgeum)

