from random import randint

# 무작위로 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    # 코드를 입력하세요
    computernumbers = []
    i = 0
    while len(computernumbers) < 6:
        new_number = randint(0, 45)

        # 새로운 수 나올때까지 다시 뽑기
        while new_number in computernumbers:
            new_number = randint(1, 45)
        computernumbers.append(new_number)
    computernumbers = sorted(computernumbers)
    return computernumbers

# 보너스까지 포함해 7개 숫자 뽑기
def draw_winning_numbers(computernumbers):
    number_row = []
    input_row = computernumbers
    bonus_number = randint(1, 45)
    input_row.append(bonus_number)
    number_row = input_row
    return number_row

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
#def count_matching_numbers(list1, list2):
    # 코드를 입력하세요

# 로또 등수 확인하기
#def check(numbers, winning_numbers):
    #코드를 입력하세요

randomnumber = generate_numbers()
print(randomnumber)
test_list = []
test_list = draw_winning_numbers(randomnumber)
print(test_list)