### Tuple

x=(1,2,3)
y=('a','b','c')
z=(1,"hello","there")

print(x+y)
print('a' in y)          # y에 'a'가 있는지
print(z.index(1))        # z에 1이 몇번째인지

# list와 tuple의 차이점:
# tuple은 assignment(값 바꿔치기' x(2)=10)이 안됨; immutable(불변) <-> mutagle(가변)

