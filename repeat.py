# while문
#while <조건문> :
#    <수행할 문장1>
#    <수행할 문장2>
#    <수행할 문장3>
#    <수행할 문장4>

treeHit = 0
while treeHit < 10:
    #treeHit = treeHit + 1
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")


coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)

# for문
# for 변수 in 리스트[배열] ( 튜플, 문자열 ):
#    <수행할 문장1>
#    <수행할 문장2>
#    <수행할 문장3>
#    <수행할 문장4>

str = "abcdefg"
for char in str:
    print("char -> type[{type}]".format(type=type(char)))
    print("char -> [{value}]".format(value=char))

tuList = [ (1, 2), (3, 4), (5, 6) ]

for tu in tuList:
    print("tu -> [{value}]".format(value=tu))
    print("tu -> [{value}]".format(value=tu))

for (first, last) in tuList:
    print("first -> [{value}]".format(value=first))
    print("last  -> [{value}]".format(value=last))
    print("first + last -> [{value}]".format(value=first + last))


marks = [ 90, 25, 67, 45, 80 ]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

# range(1, 11)
# 1 <= x < 11

sum = 0
for i in range(1, 11):
    sum = sum + i
print("sum => [%d]" % sum)


for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end = " ")
    print('')
