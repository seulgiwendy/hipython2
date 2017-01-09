def is_palindrome(word):
    word_list = list(word)
    i = 0
    length_check = len(word_list)
    range_check = int(len(word_list)/2)
    for i in range (range_check):
        if (word_list[i] == word_list[(length_check-i)-1]):
            result = True
        else: result = False
    return result

print(is_palindrome('racecar'))
print(is_palindrome('토마토'))
print(is_palindrome("권수빈"))
    # 코드를 입력하세요.
