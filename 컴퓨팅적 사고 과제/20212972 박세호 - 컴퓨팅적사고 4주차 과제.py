
# 1.
현재시간 = int(input("지금 몇 시인가요? : "))
이전시간 = 현재시간 - 6
if 이전시간 < 0:
    이전시간 = 이전시간 + 24
    
print("현재시간 : %d시" % 현재시간)
print("이전시간 : %d시" % 이전시간)


# 2.
score = int(input("시험 점수를 입력하세요 : "))

if score >= 90:
    print("시험을 아주 잘 봤군요. 축하합니다.")
elif score >= 80:
    print("시험을 괜찮게 봤군요. 수고했어요.")
elif score >= 70:
    print("시험을 좀 못봤군요. 다음에는 잘 봐요.")
else:
    print("완전히 망했군요.")


# 3.
year = int(input("값을 입력하세요 : "))   

if year % 400 == 0:
    print("%d년은 윤년입니다." % year)
elif year % 100 == 0:
    print("%d년은 윤년이 아닙니다." % year)
elif year % 4 == 0:
    print("%d년은 윤년입니다." % year)
else:
    print("%d년은 윤년이 아닙니다." % year)


# 4.
number = int(input("정수를 입력하세요 : "))

if number > 0:
    print("%d(은)는 양수입니다." % number)
elif number < 0:
    print("%d(은)는 음수입니다." % number)
else:
    print("%d은 0입니다." % number)


# 5.
num = int(input("양의 정수를 입력하세요 : "))

if num > 0:
    if (num % 3 ==0):
        print("%d(은)는 3의 배수입니다." % num)
    else:
        print("%d(은)는 3의 배수가 아닙니다." % num)
else:
    print("잘못된 입력입니다.\n프로그램을 종료합니다.")


# 6.
퀴즈점수 = int(input("퀴즈는 몇 점인가요? : "))
중간점수 = int(input("중간 고사는 몇 점인가요? : "))
기말점수 = int(input("기말 고사는 몇 점인가요? : "))
최종점수 = 0.2 * 퀴즈점수 + 0.3 * 중간점수 + 0.5 * 기말점수

if 최종점수 >= 80:
    print("최종점수가 %.1f점이므로 Pass입니다." % 최종점수)
else:
    print("최종점수가 %.1f점이므로 Fail입니다." % 최종점수)

        
