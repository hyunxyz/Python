# 과일 숫자 세는 프로그램

fruit=["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아", "복숭아"]

d={}                    # create dictonary

for f in fruit:         #for loop ; f=알파벳은 통일만 되도 상관X
    if f in d:          #"사과"라는 key가 d라는 dic에 들어있어?
        d[f]=d[f]+1     #그럼 "사과" 갯수를 하나 올려줘
    else:
        d[f]=1          #민액 "사과"가 없으면. 그걸 dic에 넣고, value는 1로 만들어줘

print(d)



# 첫번째 값부터 차례대로 시작
# 1st round: d={empty} > "사과"가 없으므로, dic에 넣고 value는 1 > dic={'사과':1}
# 2nd round: d={'사과':1} > "사과"가 있으니 1+1 > dic={'사과':2}
# ...
