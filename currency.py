# 원(￦)에서 달러($)로 바꿔주는 함수
def krw_to_usd(won):
    krw = won
    usd = krw / 1000
    return usd

# 코드를 입력하세요.

# 달러($)에서 엔(￥)로 바꿔주는 함수
def usd_to_jpy(dollars):

    yen = dollars * (1000/8)
    return yen


# 코드를 입력하세요.

# 원(￦)으로 각각 얼마인가요?
amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))

# amounts를 원(￦)에서 달러($)로 바꿔주기
# 코드를 입력하세요.

woncount = 0
while(woncount < len(amounts)):
    amounts [woncount] = krw_to_usd(amounts[woncount])
    woncount += 1



# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔(￥)으로 바꿔주기
# 코드를 입력하세요.
yencount = 0
while (yencount < len(amounts)):
    amounts [yencount] = usd_to_jpy(amounts[yencount])
    yencount += 1


# 엔(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(amounts))