'''
# 확인문제 1
print("355 / 32 = %f" %(355/32))

# 확인 문제 2
print("355를 32로 나눈 몫은 %d | 나머지는 %d" %((355//32), (355%32)))

# p43
a = 5
b = 3
for x in range(10,102,10):
    y = x**2 + (b/a)*2 + (b/2*a)**2
    print(x, "-------->",       y)
    

#p48
x=5
y=7
x=y
z=10
z=x+y
print(x,y,z)

#p51
반지름 = 15
파이 = 3.141592
원의둘레 = 반지름*2*파이
원의넓이 = 반지름**2*파이
print("반지름 :", 반지름)
print("원의둘레 :", 원의둘레)
print("원의넓이 :", 원의넓이)

#p52
한국돈 = 2500000
달러 = 1175
환전액 = 한국돈//달러
남은돈 = 한국돈%달러
print("%d원을 환전하여 %d달러가 되었습니다. 남은 돈은 %d원입니다."%(한국돈, 환전액, 남은돈))

#3
x=10
y=x//3
y+=2
print(y)

#4
a=5
b=3
c=a%b
c *= 7
print(c)

#5
a= 8-3*2
b= a*2**3
c=a+b
print(c)

#6
from cmath import atan


a = 15000
b = 23000
c = 30000
print(3*a+5*b+2*c)

#7
a= 95
b = 87
c = 100
sum = a+b+c
avg = (a+b+c)/3
print("%d | %d" %(sum,avg))

#8
a = 9/5
C= 32
F = C * a + 32
print(F)

#9
a= 9.8
t = 3
V = a * t
print(V)

#10
현재가격 = 34900
인상가 = 현재가격 * 12/100
내년가격 = 현재가격 + 인상가
print("내년가격 :", 내년가격)


#11
현재가격 = 50000
미래가격 = 현재가격 * (1.06)**10
print(미래가격)
'''
#12
몇배 = (1.05)**20
print(몇배)
print(3000000 * 몇배)


