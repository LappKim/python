# dictionary 자료형
#  연관 배열 또는 Hash
#  key / value 형태
# JSON 같은 자료구조

dic = {
    "name": "Eric", "age": 30
}

print("dic['name'] => [{name}], id => [{id}]".format(name=dic["name"], id=id(dic)))

print("dic => [{dic}], id => [{id}]".format(dic=dic, id=id(dic)))


a = { 1: 'a' }
# dictionary 추가
a['name'] = "김현석"

print("a => [{a}], id => [{type}][{id}]".format(a=a, type=type(a), id=id(a)))

# dictionary 삭제

# del a[0] : key가 없어서 오류 (KeyError: 0)
del a[1]

print("a => [{a}], id => [{id}]".format(a=a, id=id(a)))

# dictionary 주의사항 - 같은 키일 때 앞에 정보 사라짐.!!
a = { 1: 'a', 1: 'b' }

print("a => [{a}], id => [{id}]".format(a=a, id=id(a)))

# Key 리스트 만들기 (keys)
# Value 리스트 만들기 (values)
a = { 'name': 'pey', 'phone': '01088399710', 'birth': '1216' }

print("keys => [{keys}], values = [{values}], id => [{id}]".format(keys=a.keys(), values=a.values(), id=id(a)))

# dictionary items() 의 return값은 tuple
print("items => [{items}], id => [{id}]".format(items=a.items(), id=id(a)))

for key in a:
    value = a[key]
    print(f"key -> [{key}], value -> [{value}]")

print("")

for key, value in a.items():
    print(f"key -> [{key}], value -> [{value}]")

# dictionary .get(key)
# key가 없으면 return값을 None
print("a.get('name') => [{value}]".format(value=a.get('name')))
print("a.get('name2') => [{value}]".format(value=a.get('name2')))
print("a.get('name2') => [{value}]".format(value=a.get('name2', '없음')))

# in 
print("'name2' in a => [{value}]".format(value=('name2' in a)))
