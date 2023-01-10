# 컴퓨팅적 사고 2주차 과제

# 1. 집 모양 그리기
import turtle as t

t.shape("turtle")
t.shapesize(3)

for i in range(3):
    t.forward(250)
    t.left(120)

t.left(180)
for i in range(3):
    t.left(90)
    t.forward(250)


# 2. input함수와 외각 패턴을 통해 오각형 그리기
import turtle as t

t.shape("turtle")
t.shapesize(3)

n = int(input("몇 각형을 그리시겠습니까? : "))
a = 360/n

for i in range(n):
    t.forward(200)
    t.right(a)


# 3. 별 그리기
import turtle as t

t.shape("turtle")
t.shapesize(3)

for i in range(5):
    t.forward(300)
    t.right(144)


# 4. 계단 모양 그리기
import turtle as t

t.shape("turtle")
t.shapesize(3)

for i in range(4):
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.left(90)

