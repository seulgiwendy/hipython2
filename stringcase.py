# 자리수 합 리턴
def sum_digit(num):
    numsum = 0
    question = str(num)
    for i in range(len(question)):
       numsum = numsum + int(question[i])
    return numsum

    # 코드를 입력하세요.

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.

result_sum = 1
for q in range (1000):
    result_sum = result_sum + sum_digit(q)

print(result_sum)