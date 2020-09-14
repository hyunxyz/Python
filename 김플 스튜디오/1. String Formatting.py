name = '현지'
number = 7
food = '피자'

# print('제 이름은 ' + name + '입니다. 좋아하는 숫자는 ' + str(number) + '이고 좋아하는 음식은 ' + food + '입니다.')
# too wordy

print('제 이름은 %s입니다. 좋아하는 숫자는 %d이고 좋아하는 음식은 %s입니다.' %(name, number, food))
              #문자열               #숫자 (%d로 해도 됨;)
# 더 편해졌지만 마지막에 + '제 이름은 %s입니다'가 추가반복되면 에러뜸 bc %()안에는 3개뿐이기 때문

print('제 이름은 {0}입니다. 좋아하는 숫자는 {1}이고 좋아하는 음식은 {2}입니다.' .format(name, number, food))
print('제 이름은 {0}입니다. 좋아하는 숫자는 {1}이고 좋아하는 음식은 {2}입니다. 제 이름은 {0}입니다.' .format(name, number, food))
# 변수가 정해진 index로 들어가기 때문에 문장이 길어지거나 반복되도 문제X; {0}=name 

print(f'제 이름은 {name}입니다. 좋아하는 숫자는 {number}이고 좋아하는 음식은 {food}입니다.')
# the simplest/intuitive form ***
