# 컴퓨팅적 사고 2주차 과제

# 1. 문제 1
원금 = 5000000
이자율 = 3.25/100
원리금 = (원금*이자율) +원금
print("원리금 = %d" % (원리금))


# 2. 문제 2
원달러환율 = 1135
원 = 1500000
달러 = 원/원달러환율
print("보유한 달러 = %d" % (달러))


# 3. 문제 3
원금 = 15000000
이자율 = 3.25/100
이자 = 원금*이자율*3
소득세율 = 15.4/100
세금 = 이자 * 소득세율
원리금 = 원금 + 이자 - 세금
print("원리금 = %d" % (원리금))


# 4. 다각형 그리기 기본

# 1) 정삼각형
import turtle as t

t.shape("turtle")
t.shapesize(3)

t.forward(300)
t.left(120)
t.forward(300)
t.left(120)
t.forward(300)
t.left(120)

# 2) 정사각형
import turtle as t

t.shape("turtle")
t.shapesize(3)

t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)

# 3) 정오각형
import turtle as t

t.shape("turtle")
t.shapesize(3)

t.forward(160)
t.left(72)
t.forward(160)
t.left(72)
t.forward(160)
t.left(72)
t.forward(160)
t.left(72)
t.forward(160)
t.left(72)

# 4) 정육각형
import turtle as t

t.shape("turtle")
t.shapesize(3)

t.forward(150)
t.left(60)
t.forward(150)
t.left(60)
t.forward(150)
t.left(60)
t.forward(150)
t.left(60)
t.forward(150)
t.left(60)
t.forward(150)
t.left(60)


# 5. 다각형 그리기 - 반복문 이용

# 1) 정삼각형
import turtle as t

t.shape("turtle")
t.shapesize(3)

for i in range(3):
    t.forward(300)
    t.left(120)

# 2) 정사각형
import turtle as t

t.shape("turtle")
t.shapesize(3)

for i in range(4):
    t.forward(300)
    t.left(90)

# 3) 정오각형
import turtle as t

t.shape("turtle")
t.shapesize(3)

for i in range(5):
    t.forward(150)
    t.left(72)

# 4) 정육각형
import turtle as t

t.shape("turtle")
t.shapesize(3)

for i in range(6):
    t.forward(150)
    t.left(60)


# 6. 다각형 그리기 - input함수와 외각의 패턴을 이용

# ex)정육각형 
import turtle as t

t.shape("turtle")
t.shapesize(3)

n = int(input("몇 각형을 그리시겠습니까? : "))
a = 360/n

for i in range(n):
    t.forward(150)
    t.left(a)



