reference_txt = open('chicken.txt','r')
amount = 0
for line in reference_txt:

    data = (line.strip().split(": "))
    amount = amount + int(data[1])

lastday = line[:2]
result = int(amount / int(lastday))
print("이번달 매출의 평균은 %d원입니다." % (result))