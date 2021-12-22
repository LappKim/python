# def 함수명 (매개변수):
#     <수행할 문자1>
#     <수행할 문자2>
# 
#     return 
# 

def sum(a, b) :
    #result = a + b
    #return result
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))
    return

print(sum(1, 2))


def say():
    return "hi"

print(say())

myList = [ 1, 2, 3 ]
print(myList.append(4))

print(myList.pop())
print(myList.pop())

## * 는 list
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(sum_many(1,2,3,4,5,6,7,8,9,10))

## ** key ward arguments
def print_kwargs(**kwargs):
    for key in kwargs:
        value = kwargs[key]
        print(f"key=>[{key}], value=>[{value}]")
    return

# for key in a:
#     value = a[key]
#     print(f"key -> [{key}], value -> [{value}]")

# print("")


print(print_kwargs(name = 'Kim Hyunseok', age = 47))

# 결과값은 하나이다.
def sum_and_multi(a, b):
    return a+b, a*b, a-b

# 튜블로 return
print("sum_and_multi(2, 3) => %s" % str(sum_and_multi(2, 3)))
print("sum_and_multi(2, 3)[0] => %s" % str(sum_and_multi(2, 3)[0]))
print("sum_and_multi(2, 3)[1] => %s" % str(sum_and_multi(2, 3)[1]))
print("sum_and_multi(2, 3)[2] => %s" % str(sum_and_multi(2, 3)[2]))

# argument의 default value
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % (name))
    print("나이은 %d살입니다." % (old))
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself('김현석', 47)
say_myself(name='김현석', old=47)
say_myself(old=47, name='김현석', man=False)
