### Dictionary
# key와 value로 이루어짐

x={
    "name":"현지",   #key : value
    "age":28,       
    0:"코딩중",     
}

print(x)

print(x["name"])    #"name"의 value은?
print(x["age"])
print(x[0])
  
print("age" in x)   #x에 "age"가 들어있나요?

print(x.keys())     #dic에 있는 모든 key를 보여줘
print(x.values())   #dic에 있는 모든 value를 보여줘


for key in x:
    print("key:"+str(key))
    print("value:"+str(x[key]))
              #value = x[ ]


x["name"]="소풍이"     #assignment(바꿔치기)
print(x)


x["school"]="Boston U"   #key,value 추가 
print(x)


