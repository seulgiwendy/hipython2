# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    if n < 10:
        return n
    digit = str(n)
    return sum_digits(int(digit[0])) + sum_digits(int(digit[1:]))

print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

