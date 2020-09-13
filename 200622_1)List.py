##### 자료구조

### List: element 여러개를 grouping 할 때

x=[4,2,3,1]
#  0 1 2 3 번째 자리에 있음 (항상 코딩은 0부터 시작)
y=["hello","world"]
z=["hello",1,2]


print(x)
print(y)
print(z)
print(x+y)

print(x[0])         #x의 0번쨰 elmt 보여줘

q=sorted(x)         #정렬
print(q)

r=sum(x)            #합
print(r)

for n in x:         #list에 있는 elmt 하나씩 보여줘***
    print(n)

for c in y:
    print(c)

print(x.index(3))    #위치찾기; x안에 3이 어디있나
print(y.index("hello"))

print("hello" in y)  #y에 hello가 있는지

if "hello" in y:
    print("hello 있어요")


x[3]=10              #assignment (값 바꿔치기)
print(x)

num_elements=len(x)  #length (몇 가지 elmt?)
print(num_elements)

q=sorted(x)          #정렬; 자리 바꿔치기한 결과값의 정렬인듯..
print(q)


