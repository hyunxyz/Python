###name 변수를 "현지"로 고정시키지 않고 object를 만들때 

class Person:
    def __init__(self, name, age):          #initializae
        self.name  = name
        self.age = age

    def say_hello(self, to_name):     #(누구를)이라는 새로운 인자 추가
        print("안녕! " + to_name + " 나는 " + self.name)
    
    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + " 살이야")
                                                #age는 숫자타입의 변수라, 숫자>문자열 타입으로 캐스팅 필요
isabel = Person("현지", 28)
isabel.introduce()



### 상속(inheritance): 공통 class가 있고, 아래에 세부 class 만들 때

class Police(Person):     #Police이란 class가 Person이란 class를 상속
    def arrest(self, to_arrest):
        print("넌 체포됐다, " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야겠다: " + to_program)

isabel = Person("현지", 28)
ted = Police("동규", 29)
jeff = Programmer("창현", 23)

ted.introduce()      #Police이라는 class안에 함수를 arrest 하나밖에 안넣었으나 introduce 함수를 쓸 수 있게됨
ted.arrest("도둑")
jeff.introduce()
jeff.program("이메일 클라이언트")