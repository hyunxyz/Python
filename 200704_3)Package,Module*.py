### Package (library) : Module의 합 ;ex.날씨 정보를 알아보는 패키지
### 내가 만든 package를 공유 <-> 반대로 남이 만든 걸 갖다 쓸 수 있음
### Module: 코드가 들어있는 파일. 이 코드가 모여서 한 기능을 구현함

# animal package
# dog, cat modules
# dog, cat modules can say "hi"

#패키지를 만들려면 폴더가 필요

from animal import dog    # animal 패키지에서 dog 모듈을 갖고와
from animal import cat   

#i
d = dog.Dog()       # instnace
d.hi()

c = cat.Cat()
c.hi()

#ii (좀 더 간단히 하고싶다면?)
from animal import *     # animal 패키지가 갖고 있는 모듈을 다 불러와

d = Dog()
c = Cat()

d.hi()
c.hi()

