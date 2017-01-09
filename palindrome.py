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

word_input = input("검사하고자 하는 단어를 입력하세요:")
print(is_palindrome(word_input))