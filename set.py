# 집합 자료형
## 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형
## 중복을 허용하지 않는다.
## 순서가 없다 (Unordered)

s1 = set([1, 2, 3])

s2 = { 1, 2, 3 }

print("s1 -> [{value}], type -> [{type}]".format(value=s1, type=type(s1)))

print("s2 -> [{value}], type -> [{type}]".format(value=s2, type=type(s2)))


#list -> set(중복제거) -> list
l1 = [ 1, 2, 2, 3, 3, 4, 5, 6 ]
newList = list(set(l1))

print("l1 -> [{value}], type -> [{type}]".format(value=l1, type=type(l1)))

print("newList -> [{value}], type -> [{type}]".format(value=newList, type=type(newList)))

l2 = set("Hello")
print("l2 -> [{value}], type -> [{type}]".format(value=l2, type=type(l2)))

# 교집합/합집합/차집합
s1 = set([ 1, 2, 3, 4, 5, 6 ])
s2 = set([ 4, 5, 6, 7, 8, 9 ])

print("교집합/합집합/차집합")
print("s1 -> [{value}], type -> [{type}]".format(value=s1, type=type(s1)))
print("s2 -> [{value}], type -> [{type}]".format(value=s2, type=type(s2)))

# 교집합
print("교집합")
print("s1 & s2 -> [{value}]".format(value=(s1 & s2)))
print("s1.intersection(s2) -> [{value}]".format(value=s1.intersection(s2)))

# 합집합
print("합집합")
print("s1 | s2 -> [{value}]".format(value=(s1 | s2)))
print("s1.union(s2) -> [{value}]".format(value=s1.union(s2)))

# 차집합
print("차집합")
print("s1 - s2 -> [{value}]".format(value=(s1 - s2)))
print("s2 - s1 -> [{value}]".format(value=(s2 - s1)))

print("s1.difference(s2) -> [{value}]".format(value=s1.difference(s2)))
print("s2.difference(s1) -> [{value}]".format(value=s2.difference(s1)))

# 집합에 추가
s1.add(7)
print("s1 -> [{value}], type -> [{type}]".format(value=s1, type=type(s1)))

s1.update([8, 10])
print("s1 -> [{value}], type -> [{type}]".format(value=s1, type=type(s1)))

# 집합에서 빼기
s1.remove(7)
print("s1 -> [{value}], type -> [{type}]".format(value=s1, type=type(s1)))
