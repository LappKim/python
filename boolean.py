# 참(True)
# 거짓(False)

a = True

print("a -> [{value}], type=[{type}]".format(value=a, type=type(a)))

a = 1

if a == 3:
    print('참')
else:
    print('거짓')

# 값         | 참 or 거짓
# "python"   | 참
# ""         | 거짓
# [1, 2, 3]  | 참
# []         | 거짓
# ()         | 거짓
# {}         | 거짓
# 2          | 참
# 1          | 참
# 0          | 거짓
# None       | 거짓

if 0:
    print('참')
else:
    print('거짓')

if 2:
    print('참')
else:
    print('거짓')

if "":
    print('참')
else:
    print('거짓')

if "aaa":
    print('참')
else:
    print('거짓')

a = [ 1, 2, 3, 4, 5 ]
while a:
    b = a.pop()
    print("a => [{value1}], pop value => [{value2}]".format(value1=a, value2=b))

