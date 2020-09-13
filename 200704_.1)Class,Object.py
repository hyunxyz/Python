#class = 함수 + 변수 (빵틀)
#object / instance= class를 이용해서 만들어낸 물체 (빵)

class Person:
    name="현지"
    def say_hello(self):
        print("안녕! 나는 "+self.name)

p = Person ()  #p라는 object 생성
p.say_hello()  #say_hello라는 함수

