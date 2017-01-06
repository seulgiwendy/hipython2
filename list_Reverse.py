numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
# 코드를 입력하세요.
number_reverse = numbers
temp = numbers

print(len(numbers))
print(str(temp))
print(str(number_reverse))

print(number_reverse[0])
print(number_reverse[len(numbers)-1])
number_reverse[0] = numbers[len(numbers)-1]
number_reverse[1] = numbers[len(numbers)-2]
number_reverse[2] = numbers[len(numbers)-3]
number_reverse[3] = numbers[len(numbers)-4]
number_reverse[4] = numbers[len(numbers)-5]
number_reverse[5] = numbers[len(numbers)-6]
number_reverse[6] = numbers[len(numbers)-7]
print(str(number_reverse))

#temp = numbers[left_index]
#numbers[left_index] = numbers[right_index]
#numbers[right_index] = temp