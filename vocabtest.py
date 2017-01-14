#이제 단어 암기를 위해서 학생들을 퀴즈해주는 프로그램을 만들고 싶습니다.
# vocabulary.txt의 첫 줄부터, 콘솔에 한국어 뜻을 알려주면 학생이 영어 단어를 입력하는 방식입니다. 맞는 답이 나오면 맞았습니다!가 출력되고 틀린 답이 나오면 틀렸습니다.
# 정답은 OOO입니다. 형식으로 나옵니다.

in_file = open('vocabulary.txt', 'r')


for line in in_file:
    data = line.strip().split(": ")

    eng = data[0]
    kor = data[1]

    answer = input("%s: " %(eng))
    if (answer == kor):
        print("맞았습니다!")
    else:
        print("틀렸습니다. 정답은 %s입니다." % (kor))

in_file.close()






