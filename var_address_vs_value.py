from copy import copy

# 변수 대입은 reference만 기록

a = [1, 2, 3]
b = a
b[1] = 4


print("1. a => [{value}], id of a => [{id}]".format(value=a, id=id(a)))
print("1. b => [{value}], id of b => [{id}]".format(value=b, id=id(b)))

# 값을 넣고 싶으면 slice 하든가
a = [1, 2, 3]
b = a[:]
b[1] = 4

print("2. a => [{value}], id of a => [{id}]".format(value=a, id=id(a)))
print("2. b => [{value}], id of b => [{id}]".format(value=b, id=id(b)))

# copy()를 사용한다.
a = [1, 2, 3]
b = copy(a)
b[1] = 4

print("3. a => [{value}], id of a => [{id}]".format(value=a, id=id(a)))
print("3. b => [{value}], id of b => [{id}]".format(value=b, id=id(b)))

