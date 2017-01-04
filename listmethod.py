# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
# 코드를 입력하세요
a = 1
app = 1
while (a <= 10):
    numbers.append(app)
    app += 1
    a +=1


print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요


b = 0
target_range_odd = int(len(numbers)/2)
print(target_range_odd)

while (b < target_range_odd):
    print(b)
    del numbers[b]
    b += 1

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요

numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요

numbers = sorted(numbers)
print(numbers)