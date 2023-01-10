# [While문] 

# 1.
a = 1
sum = 0
while(a<=100) :
    sum = sum + a
    a = a + 1
print("1부터 100까지의 합계는 %d입니다." % (sum))


# 2.
i = 1
n = int(input("양의 정수를 입력하세요 : "))
if (2 <= n <= 9) :
    while (1 <= i <= 9) :
        print("%d * %d = %d" % (n, i, n * i))
        i = i + 1
else :
    print("잘못된 값이 입력되었습니다.")
print("프로그램을 종료합니다.")


# 3.
a = 30
sum = 0
while (30 <= a <= 70) :
    if (a % 3 == 0) :
        sum = sum + a
    a = a + 1
print("30부터 70까지의 정수 중 3의 배수의 합계 : %d" % (sum))



# [for문]

# 1.
n = int(input("양의 정수를 입력하세요 : "))
if (2 <= n <= 9) :
    for i in range (1,10,1) :
        print("%d * %d = %d" % (n, i, n * i))
else :
    print("잘못된 값이 입력되었습니다.")
print("프로그램을 종료합니다.")


# 2.
A = int(input("양의 정수를 입력하세요 : "))
B = int(input("양의 정수를 입력하세요 : "))
sum = 0
if (A > B) :
    print("프로그램을 종료합니다.")
else :
    for i in range (A, B + 1, 1) :
        sum = sum + i
    print("%d부터 %d까지의 합은 %d이다." % (A,B,sum))


# 3.
sum = 0
for i in range(100, 151, 1) :
    if (i % 7 == 0) :
        sum = sum + i
print("100부터 150까지의 정수 중 7의 배수의 합계 : %d" % (sum))


# 4.
sum = 0
for i in range(50, 101, 1) :
    if (i % 3 == 0 or i % 5 ==0) :
        sum = sum + i
print("합계는 %d이다." % (sum))

