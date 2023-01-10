'''
# p74
x= int("2019")
y= int("2000")
print(x-y)
print(type(x))

x = "2019"
y = "2000"

a=int(x)-int(y)
print(a)
print(type(a))
print(type(x))

#p81
text = "HELLO"
for c in text:
    print(c, "--->", ord(c))
    
print("이름 입력: ")
a = input()
print("안녕 ~", "%s씨"%(a), "반가워요")

#p98
b = int(input("주차시간 입력 : "))
a = b//15
주차요금 = a * 1000
print("주차시간 = %d | 주차요금 = %d" %(b,주차요금))


#p101
a = float(input("몇 마일 : "))
mile = 1.60934
b = a * mile
print(b)

ass = input("")
text = "나는 %s이다 시발" %(ass)
print(text)
'''
sum = 0
def post(x,y,z):
    for i in range (x,y,z):
        sum += i
    return sum

a = post(1,5,1)
print(a)
 