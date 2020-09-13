print("Hellow World")



###변수 (variable)
x=4                            #숫자타입
y="4"                          #문자타입
q=6

print(x**q)                    #제곱
print(x%q)                     #mod: 남는값




###문자열 (type)
print("안녕"+" 뭐해")

z="""
잠온다
하지만 참는다..!
"""
print(z)
print("안녕?"+str(4))

#캐스팅하다 (문자/숫자 통일)
print(str(x)+y)                 #str:문자
print(x+int(y))                 #int:숫자




###조건문
if 2>1:
  print("good job")
if not 2>1:                     #~가 아니라면
  print("try again")

if 1>0 and 2>1:                 #둘 다 만족해야하는 조건
  print("both")
if 0>1 or 2>1:                  #둘 중 하나만 만족
  print("either")

  if x>2:                       #위에서부터 차례대로
    print("bigger")
  elif x==4:                    #바로 위 조건이 부합하지 않아야 equal..?
      print("equal")
  elif x<=5:
    print("smaller than")
  else:                         #그렇지않으면
    print("Hi")





###함수 (function)


def chat(name1,name2,age):      #부분 변경
    print("%s: 몇 살이야?"%name1)
    print("%s: 난 %d살"%(name2,age))

chat("C","D",10)

      #반복하려면 chat()

def dsum(a,b):
    result=a+b
    return result 

c=dsum(1,2)
print(c)




### Review Practice
# 먼저 이름과 나이를 받아라
# 나이가 10살 미만이면 "안녕"이라고 말해라
# 나이가 10살~20살 사이면 "안녕하세요"라고 말해라
# 그 외에는 "안녕하십니까"라고 말해라

def sayHello(name,age):
    if age<10:
        print("안녕,"+name)
    elif age<=20 and age>=10:
        print("안녕하세요,"+name)
    else:
        print("안녕하십니까,"+name)

sayHello("고니",8)
sayHello("워니",12)
sayHello("져니",30)




###반복문 (for, while)

for i in range(3):           #for loop
    print(i) #이건 지워도 됨
    print("A: 안녕 뭐해?")
    print("B: 그냥 있어")

for i in range(100):         #n만큼 반복 + break로 조건부 정지
    print(i)
    print("A: 안녕 뭐해?")
    print("B: 그냥 있어")

    if i>2:
        break

for i in range(3):           #n만큼 반복 + break로 조건부 정지
    print(i)
    print("A: 안녕 뭐해?")
    print("B: 그냥 있어")

    if i==1:
      continue               #특별한 조건에서 이 다음 문장이 안나오게함

    print("C: 안녕 A,B야")

  
i=0
while i<3:                   #조건문가능
    print(i)                 #i=0
    print("A: 안녕 뭐해?")
    print("B: 그냥 있어")
    i=i+1                    #i=0+1=1
                             #여기서 110번으로 올라가서 i=3<3이 되서 멈출때까지 반복

i=0
while True:                  #무햔루프 + break로 조건부 정지
    print(i)
    print("A: 안녕 뭐해?")
    print("B: 그냥 있어")
    i=i+1
    
    if i>2:
        break

